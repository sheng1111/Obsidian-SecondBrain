# Knowledge policy

## Model and destinations

Use the lifecycle Capture → Distill → Connect → Verify → Review. Capture must stay frictionless, but captures are processing material rather than permanent presentation. Folders describe purpose and lifecycle; properties and meaningful links describe subjects.

- `00 Inbox`: captures that are not yet reliably understood or integrated.
- `10 Sources`: concise, traceable external evidence and the claims it supports or challenges.
- `20 Knowledge`: reusable synthesis centered on a concept, question, or decision.
- `30 Projects`: work with an outcome or ongoing execution context. Courses live in `30 Projects/Courses/`.
- `90 Archive`: retained material removed from routine use.
- `99 System`: local views, templates, and system resources.
- `Attachments`: source files and media. Never delete them without explicit authorization.

A summary of one external item remains a Source. Create or update Knowledge when material supports a cross-source comparison, reusable model, decision framework, or a conclusion connected to practical context. Clearly label AI-generated synthesis and cite its evidence; never imply that the user already accepts it.

## Stable properties

Use only the properties the note actually needs:

```yaml
status: reference
type: source
areas:
  - learning
topics:
  - searchable subject
entities:
  - named entity
source: https://example.com/original
captured: YYYY-MM-DD
review_after: YYYY-MM-DD
```

Valid `status` values are `inbox`, `active`, `reference`, and `archived`. Valid `type` values are `source`, `knowledge`, and `project`. `areas`, `topics`, and `entities` are YAML lists; dates use `YYYY-MM-DD`. Omit unknown properties instead of inventing values.

Start `areas` with the stable responsibility domains `work`, `learning`, and `life`. Technologies, disciplines, and subjects belong in `topics`. Put only retrieval-useful named people, organizations, products, tools, places, repositories, and works in `entities`. Search existing properties, titles, aliases, and synonyms before adding values. Do not create notes or wikilinks merely because an entity was extracted. Do not duplicate topics or entities as tags.

Keep unclear personal fragments in the Inbox without forcing a `type`. Do not create a generic Notes category unless a recurring need justifies it.

## Source-note outcome

A Source is organized around one identifiable evidence unit. Use only the sections the material needs:

- `## Summary`: what the source covers, why it may matter, and its limitations.
- `## Verifiable Points`: claims that support, complement, or challenge Knowledge, with attribution.
- `## User Context`: only context that changes use, interpretation, or action; exact wording is optional unless consequential.
- `## Relationships`: meaningful support, complement, conflict, or application links.
- `## Sources`: stable original URLs, primary verification sources, and necessary attachment embeds.

Do not retain copied full pages, comment dumps, link previews, OCR transcripts, or processing prompts by default. Keep a quotation only when the source cannot be reconstructed, exact wording is material, or it records a commitment or work fact.

## Knowledge-note outcome

Name Knowledge after the concept, question, or decision likely to be retrieved later, not after a single post. Use sections as needed:

- Label an AI-created or substantially rewritten note with an `AI synthesis` callout. State that it is revisable and does not represent user endorsement.
- `## Core Understanding`: the current synthesis and its boundary conditions.
- `## Source Comparison`: agreement, conflict, evidence strength, and anecdotal limitations.
- `## Applications`: decisions, steps, checklists, or next experiments.
- `## System Prompt`: a ready-to-paste behavior layer when the Knowledge contains reusable decision rules or domain guidance.
- `## Open Questions`: gaps, unstable facts, and items requiring user experience or further evidence.
- `## Sources`: links to Sources, Projects, work reviews, and necessary primary references.

User drafts may be normalized into clear language and structure. Preserve URLs, code, filenames, necessary quotations, and proper nouns. Keep exact user wording only when tone, commitment, or personal experience affects interpretation; label it as original user context.

## Knowledge System Prompts

A System Prompt is the executable interface to a Knowledge note, not a required decoration or a one-off user request. It is copied into another AI's system or custom-instructions field so the Knowledge governs future related requests.

- Create it only when the note provides a reusable way to reason, decide, review, advise, or act across future requests.
- Make it work immediately after copy and paste without starting an unsolicited task. Define the AI's role, applicable scope, decision process, evidence and uncertainty rules, safety or authorization boundaries, and useful response behavior.
- Tell the AI to use subsequent conversation, selected text, attachments, or workspace context when relevant. If a future request lacks critical context, ask one natural question or at most three short questions at once; do not require the user to reformat information the AI can infer.
- Preserve flexibility: adapt the response to the future request instead of forcing every interaction into one fixed deliverable. Specify an output shape only when it materially improves quality or safety.
- Keep it model-neutral unless the task genuinely depends on a product-specific capability.
- Do not refer to the Knowledge note as if the receiving AI can read it. Include the actionable rules the AI actually needs, while avoiding a full duplicate of the note.
- Merge legacy sections such as “Prompt Template,” “Reusable Prompt,” “Goal Template,” or “Agent Task Template” into one System Prompt section. When the underlying knowledge changes, revise it in place rather than appending another version.

## Reliability rules

- **URLs:** Use a reliable reader to verify title, source, and subject. Do not infer content behind login, paywall, permission, network, or availability failures. Keep one actionable unresolved marker and a near review date.
- **Signed images:** Save only material diagrams, screenshots, original works, or evidence before a signed URL expires. Verify the local file and source page, then remove the unstable URL. Do not download decorative previews, avatars, ads, or tracking pixels.
- **Images, PDFs, and attachments:** Classify only after reliable inspection. Keep the file and reference unresolved when the content cannot be confirmed. Never delete orphaned attachments automatically.
- **Video:** Summarize content only when reliable description, subtitles, or transcript are available. Otherwise record confirmed metadata and mark the missing evidence.
- Keep source claims attributed. Do not present inference as fact or as user understanding.

## Lifecycle and review

- `active`: likely to be used within days or weeks; review in roughly 14–30 days.
- `reference`: useful for future retrieval without a current action; review in roughly 90–180 days.
- `archived`: outdated or superseded material retained for traceability.

Use `active` only when the capture or project context shows a current action. Time-sensitive tutorials, releases, prices, policies, news, and event details need shorter review cycles. A due review does not automatically imply archival.

## Courses and work reviews

Store each course in its own folder under `30 Projects/Courses/`, with one course hub and one note per lesson. Attachments remain in `Attachments`. A lesson summary remains source material until it produces reusable Knowledge.

Move work reviews to `30 Projects/Work Reviews/<year>/` even when they span several projects. Preserve auditable facts, outcomes, blockers, plans, and necessary wording while removing capture noise. Maintain one annual overview that separates reported state, plans copied from reviews, and AI-generated recommendations.

Recommendations should prioritize three to five concrete features, tools, or automations supported by repeated work evidence. For each, state what to build, the problem, MVP, and acceptance criteria. Mark unsupported needs as assumptions. Keep human confirmation, auditability, and permissions in sensitive workflows. Use [technology-radar.md](technology-radar.md) for current research.

## Duplicates and connections

Treat identical URLs, alternate shares, and similar content as candidates, not automatic duplicates. Select the most complete Source or concept-centered Knowledge note as canonical, then merge unique information and necessary context. In incremental mode, archive redundant captures after linking them. During an explicitly authorized full refactor, absorbed text captures may be removed only when the canonical result is complete and recoverable. Attachments remain protected.

Add a wikilink only when a Source supports or challenges Knowledge, two Knowledge notes have a meaningful conceptual relationship, or a Project actually uses the material. Prefer no link over a weak one, and do not create empty notes for graph density.
