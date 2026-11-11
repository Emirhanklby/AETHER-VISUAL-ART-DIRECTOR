# Selected concept to final image — mandatory director gate

## Before generation: record the selected-concept brief

Keep a short internal note, not a mandatory user approval step:
- Concept name and the core creative idea in one sentence.
- Three to five observable defining features. Mark which are essential to recognizing the concept.
- Spatial hierarchy: hero, supporting subjects, copy, scale, placement and negative space.
- Intended camera, light, materials, palette and typographic character.
- Mandatory source identity, exact copy, footer reserve and no-line constraints.
- Allowed variation versus details that must remain stable; include any explicit user selection.
- Concept-selection scores and rationale, if actually used, labelled as pre-production estimates.

Define visible features, not vague adjectives such as “premium” or “creative.” Do not add new obligations or fabricated product claims. Keep simple edits proportional: reuse the approved idea and change only what the user requested. If the user explicitly changes the concept, update this note before production; do not silently redefine it to fit a generated result.

## In the production prompt

Carry the chosen idea and all essential defining features into the ChatGPT Image brief, including spatial relationships and intended focus. Do not merely mention the concept title. Do not dilute it by adding elements from rejected alternatives. Retain the image-only production boundary and the existing footer/no-line rules.

## After generation: assess the actual image

Inspect the returned image when accessible. For each defining feature, note internally:

| Intended feature | Observed visual evidence | Status | Necessary correction |
|---|---|---|---|
| A specific feature from the selected brief | What is actually visible in the image | Matched / partial / missing / unverified | Targeted edit or none |

Judge the actual pixels rather than the prompt, a tool success message, or the concept's original score. Small decorative differences within allowed variation do not fail the gate. An essential feature that is absent, contradicted or materially weakened does fail, even when the result is attractive. A nonessential difference may pass only when it stays inside allowed variation and preserves the idea.

If concept selection used numerical scoring, keep two distinct records: **concept estimate** and **observed execution assessment**. Assess the image on the same applicable six criteria in `concept-evaluation.md`, using evidence from the image and the verified brief. Mark a criterion unverified when evidence is unavailable; do not invent a rating or full total. Scores are provisional art-direction judgement, not objective measurement. No high total can override a lost essential concept feature or other hard blocker. Without selection scoring, feature-based comparison is sufficient; do not introduce score theater for a tiny edit.

## Correct and recheck

For concept drift, name the missing or changed feature and request a focused ChatGPT Image edit using the current output and appropriate original references. Preserve the approved regions and exact copy. Recheck the whole frame after each correction, including previous passes, because edits can drift. Do not switch to code, external assembly, or a different concept as a shortcut.

Accept as complete only when the essential features match, remaining differences are within allowed variation, and the normal quality checklist passes. If inspection is impossible, mark fidelity unverified. If correction remains unsuccessful, disclose the specific mismatch instead of claiming completion or repeating indefinitely. Keep internal comparison notes and scores out of the final response unless requested.

## Example

Selected idea: a winter/cosy-interior contrast. Essential features: the reference heater is the hero; a cool winter exterior is visible through a window; the warm interior contrasts with that exterior. A warm beige studio with no window may be beautifully lit but loses the defining contrast: fail the concept gate and restore the winter/window relationship through ChatGPT Image. Exact room furniture can vary if not otherwise locked. Keep the reserved footer empty throughout.
