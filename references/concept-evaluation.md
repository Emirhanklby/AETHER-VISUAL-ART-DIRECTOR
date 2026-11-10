# Concept Evaluation — Select the visual direction before production

**Trigger:** fresh high-impact campaign, ambiguous brief or multiple possible creative routes. Skip full scoring for tiny revisions.

Generate three **different** concepts, not three colors: one-line thesis, audience motive, source-product compatibility, hero and text regions, lighting and materials, references if actually researched, production approach and principal risks.

## Hard blockers

- invented_claim_or_price — Unsupported pricing, features or marketing claim.
- protected_reference_reproduction — Reproducing identifiable protected artwork or a near-duplicate layout.
- product_identity_compromised — Redrawing or distorting a source-locked product.
- mandatory_copy_illegible — Essential copy can't be read or safely fit.

Reject a blocked concept regardless of numerical score.

## Score with evidence (100 points)

| Criterion | Weight |
|---|---:|
| Brand and audience fit | 20 |
| Originality and conceptual strength | 20 |
| Visual hierarchy and negative space | 20 |
| Production feasibility and product fidelity | 20 |
| Accurate copy and readability | 10 |
| Format, crop and safe zones | 10 |

Rate each 0–5 and write concrete evidence; weighted score = sum(weight × rating / 5). Above 80: proceed if no blockers. 65–79: revise the weakest part and reevaluate. Below 65 or blocked: rethink. Close scores should favor source fidelity, truthful claims, and credible execution.

## Tool

~~~bash
python scripts/aether_visual.py evaluate --input examples/concepts.json --report concept-report.json
~~~

Evaluator only computes scores supplied by an agent/designer. It does not inspect visuals, research references or establish creative truth. Even a high-scored concept must pass final QA. Document the selected direction, source principles, rejected options and execution plan.
