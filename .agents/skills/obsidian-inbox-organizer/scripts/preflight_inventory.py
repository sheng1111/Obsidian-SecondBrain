#!/usr/bin/env python3
"""Read-only duplicate-candidate inventory for an Obsidian vault."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


URL_RE = re.compile(r"https?://[^\s<>()\[\]\"']+")
SOURCE_RE = re.compile(r"(?m)^source:\s*[\"']?([^\n\"']+)[\"']?\s*$")
TRACKING_KEYS = {
    "fbclid",
    "gclid",
    "dclid",
    "igshid",
    "mc_cid",
    "mc_eid",
    "mibextid",
}
VOLATILE_AUTH_KEYS = {
    "expires",
    "jwt",
    "key-pair-id",
    "policy",
    "signature",
    "token",
}
IGNORED_DIRS = {".agents", ".claude", ".cursor", ".git", ".obsidian", ".trash"}
IGNORED_FILES = {".DS_Store", ".gitkeep"}
IGNORED_ROOT_FILES = {"AGENTS.md", "CLAUDE.md", "README.md"}


def normalize_url(raw: str) -> str:
    raw = re.sub(r"\\([_~*])", r"\1", raw)
    raw = raw.rstrip(".,;:!?。；，！？")
    try:
        parts = urlsplit(raw)
        port = parts.port
    except ValueError:
        return raw
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = f"{host}:{port}"
    path = parts.path or "/"
    if path != "/":
        path = path.rstrip("/")
    query = []
    for key, value in parse_qsl(parts.query, keep_blank_values=True):
        lowered = key.lower()
        if (
            lowered.startswith(("utm_", "x-amz-", "x-goog-"))
            or lowered in TRACKING_KEYS
            or lowered in VOLATILE_AUTH_KEYS
        ):
            continue
        query.append((key, value))
    query.sort()
    return urlunsplit((scheme, host, path, urlencode(query, doseq=True), ""))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def visible_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or any(part in IGNORED_DIRS for part in path.relative_to(root).parts):
            continue
        if path.name in IGNORED_FILES or path.relative_to(root).as_posix() in IGNORED_ROOT_FILES:
            continue
        yield path


def duplicate_groups(index):
    groups = []
    for value, paths in sorted(index.items()):
        unique_paths = sorted(set(paths))
        if len(unique_paths) > 1:
            groups.append({"value": value, "paths": unique_paths})
    return groups


def build_report(root: Path):
    url_index = defaultdict(list)
    note_hash_index = defaultdict(list)
    attachment_hash_index = defaultdict(list)
    notes = []
    attachment_count = 0

    for path in visible_files(root):
        relative = path.relative_to(root).as_posix()
        if path.suffix.lower() == ".md":
            raw = path.read_text(encoding="utf-8", errors="replace")
            source_match = SOURCE_RE.search(raw)
            source = source_match.group(1).strip() if source_match else None
            urls = sorted(set(URL_RE.findall(raw)))
            if source and source.startswith(("http://", "https://")):
                urls.append(source)
            normalized = sorted({normalize_url(url) for url in urls})
            for url in normalized:
                url_index[url].append(relative)
            normalized_text = raw.replace("\r\n", "\n")
            note_hash_index[hashlib.sha256(normalized_text.encode()).hexdigest()].append(relative)
            notes.append({"path": relative, "source": source, "normalized_urls": normalized})
        elif path.suffix.lower() != ".base":
            attachment_count += 1
            attachment_hash_index[sha256(path)].append(relative)

    return {
        "summary": {"markdown_notes": len(notes), "attachments": attachment_count},
        "normalized_url_duplicate_candidates": duplicate_groups(url_index),
        "exact_note_duplicate_candidates": duplicate_groups(note_hash_index),
        "exact_attachment_duplicate_candidates": duplicate_groups(attachment_hash_index),
        "notes": sorted(notes, key=lambda item: item["path"]),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", nargs="?", default=".", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    report = build_report(args.vault.resolve())
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None, sort_keys=True))


if __name__ == "__main__":
    main()
