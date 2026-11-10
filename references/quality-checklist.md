# Premium Visual Art Director — delivery quality checklist

Run this gate on the **final artifact**, not just on its prompt or a draft. The check is complete only when all applicable checks pass or a specific inability to verify is transparently reported. Keep the internal checklist concise; surface QA details to the user only when relevant.

## Universal acceptance criteria (all commercial graphics)

- [ ] **Palette match:** Brand/design-context color choices are consistent, controlled, and appropriate for the audience. Accents reinforce, not undermine, the visual concept.
- [ ] **Style archetype:** The final matches the selected direction (editorial restraint, sculptural product hero, conceptual campaign, or a justified alternative) and does not regress to generic template/AI styling.
- [ ] **Two-second hierarchy:** One focal point dominates; the reading order is unmistakable for hero, message, required offer/price, and brand.
- [ ] **Copy accuracy:** All displayed words, punctuation, Turkish diacritics, model identifiers, numbers, prices, dates, and claims match the supplied brief exactly. No invented product attributes or promotional terms.
- [ ] **Typography:** Fonts specified in design context are actually used where supported; weight, scale, line breaks, tracking, kerning, optical alignment and mobile readability are deliberate. Never claim a font is used without confirming its presence.
- [ ] **Text contrast:** Assess against the local background directly beneath each text area, not merely the dominant background color. Aim for WCAG 2.x AA: normal text >=4.5:1; large text >=3:1 where large means >=24 CSS px regular or >=18.66 CSS px bold. For mixed/photographic backgrounds, test the darkest or lightest region behind each glyph or add a controlled scrim/solid text field. Contrast thresholds are useful design targets for graphics; formal WCAG conformance cannot be certified from an inaccessible or unmeasured image.
- [ ] **Layout rhythm:** Appropriate negative space, optical weight, margins, grouping, no cramped overlap, no unintentionally empty hole, platform safe area, and legibility at expected display scale.
- [ ] **Decorative restraint:** Every texture, light, icon, shape, flare or prop has a rationale. Remove distracting flourishes and duplicate messages.
- [ ] **Originality & preservation:** User product/reference details and logos are respected. Reference-mining influences are recorded when research was done, while protected compositions and original artwork are not duplicated.
- [ ] **Exact format:** Aspect ratio and target resolution are known; final asset is the requested size if technical verification is possible.

## Raster output: conditional checklist

Use only when an image was actually generated, edited, composited, or exported.

- [ ] Open/read **the final image file** (not just the prompt or preview) and inspect the full canvas at practical viewing size.
- [ ] Zoom into every text region and verify **every word and important symbol** visually; when lettering is untrustworthy, overlay verified editable text outside the image generator.
- [ ] Programmatically inspect pixel dimensions when tools are available; correct to the **exact requested pixels**, ideally by composition-aware crop/resize rather than stretching. Reopen the corrected final file.
- [ ] Verify image edges, logo clear space, cropping, product silhouette, distortion, sharpness, artifacts and export transparency when relevant.
- [ ] Export PNG if requested (or as an appropriate high-quality final format); don't mislabel a JPEG or preview as PNG.

## Code-rendered design: conditional checklist

Use only when delivering HTML/CSS/SVG/React/etc. Do not impose this pipeline on image-only work.

- [ ] Output works as a self-contained deliverable except for documented external fonts or user-requested libraries/assets.
- [ ] Use specified fonts and weights. Google Fonts loading is permitted if available; when offline, supply a documented fallback instead of pretending the remote font loaded.
- [ ] Render the actual code, capture a screenshot, **open/read the screenshot**, inspect details and text, and correct layout problems. If rendering is unavailable, report that limitation.
- [ ] UI elements (e.g., buttons, input outlines, active states) meet a minimum **3:1 non-text contrast** where WCAG 2.x applies. This is not a blanket rule for every decorative shape.
- [ ] Test target dimensions, overflow, responsiveness, safe zones and typographic treatment at expected viewing sizes.

## Prompt-only limitation

Check that instructions clearly specify palette, visual hierarchy, typography intent, copy, negative space, final aspect ratio/pixel target and exclusions. **A prompt is not a rendered asset:** do not mark dimensions, contrast ratios, final spelling or exact fonts as empirically verified until the output can be inspected.

## Fix-or-disclose decision

1. Fix any failed mandatory requirement (brand, copy, product integrity, readability, dimensions) before delivery whenever possible.
2. Then refine craft issues (spacing, crop, detail, texture, visual restraint) and inspect again.
3. If tools prevent actual checking, note precisely what wasn't verified. Never fabricate a QA pass.