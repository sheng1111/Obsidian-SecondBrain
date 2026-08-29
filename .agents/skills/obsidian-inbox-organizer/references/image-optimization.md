# Image optimization

When a capture contains a JPEG, PNG, or another reliably convertible raster image, a WebP derivative may be created for embeds to reduce routine loading and sync transfer size.

- The original image is source evidence. Keep it unchanged; a WebP file is a reproducible derivative, not a replacement original.
- Choose settings by use: lossy WebP may suit photographs; text screenshots, diagrams, tickets, and pixel-sensitive images need lossless or near-lossless settings. Do not automatically convert SVG, animated GIF, existing WebP, or unverified formats.
- Write to a temporary file first. Keep the derivative only after verifying that it decodes, preserves dimensions, and is smaller than the original; otherwise retain the original embed.
- Use the stable name `<original-name>.optimized.webp`. Re-running against an unchanged source must be a no-op. Preserve the original path in the Source note or attachment description.
- Because originals remain protected, describe the optimization as reducing embed transfer and rendering cost, not total vault storage.
