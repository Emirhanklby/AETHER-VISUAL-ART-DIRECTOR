# Concept Evaluation — Choose a visual direction before committing production

**Trigger:** new high-impact campaign, vague creative brief, 2–3+ possible visual routes, or when the first concept feels generic. Skip full scoring for tiny edits.

## Inputs

Generate **three different visual directions** (not three hues): each includes a one-line concept, audience motive, source-product compatibility, hero/copy zones, lighting language, creative references (when verified), principal production method and main risk.

## Hard blockers (reject regardless of score)

- `invented_claim_or_price`: adds unsupported marketing claims, prices or product functionality.
- `protected_reference_reproduction`: closely duplicates an identifiable protected artwork/layout rather than extracting general design principles.
- `product_identity_compromised`: depends on changing product identity or inventing hidden geometry.
- `mandatory_copy_illegible`: leaves essential message unreadable or impossible to fit.

## Score with evidence — 100 weighted points

| Criterion | Weight | What a high score means |
|---|---:|---|
| Brand & audience fit | 20 | Meaningfully speaks in brand's design language to audience |
| Originality & visual idea | 20 | Distinctive concept, not decorative novelty |
| Hierarchy & negative space | 20 | A clear hero, reading order and calm copy area |
| Feasibility & product fidelity | 20 | Can be closely matched through ChatGPT Image with coherent scene geometry |
| Truth, copy, legibility | 10 | Claims verified; required text can remain readable |
| Format, crop, safe zones | 10 | Can survive the target platform's actual crops |

For each criterion, assign a 0–5 rating **with a concrete sentence of evidence**; `weighted_score = Σ (weight × rating/5)`.

- `80–100`: proceed if no blockers.
- `65–79`: improve weakest dimension, then re-score.
- `<65` or blocked: rethink; do not force a weak concept.

Numbers are **provisional creative estimates**, not measurement of actual visual quality. The final rendered ad still needs normal QA. When aesthetic difference is close (within ~5 points), prefer the route with stronger product truth, brand fit and plausible execution over score theater.

## Decision

Reject concepts that fill the bottom footer reserve or introduce decorative lines around typography. Select and record the strongest route internally with a brief rationale. Use this as creative judgement only; do not invoke a scoring script. Produce the chosen image through ChatGPT Image.

## Carry the decision into production

After selection, record the selected-concept brief in `concept-fidelity.md` before generating. Transfer its defining visible features into the production prompt. After generation, compare the actual image against that brief and assess execution separately from this pre-production score. A high concept score cannot certify the generated result; a high execution total cannot excuse a missing essential concept feature. Follow the concept-fidelity gate before acceptance.
