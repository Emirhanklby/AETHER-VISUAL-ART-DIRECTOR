# Module 03 — Advanced Product Fidelity

**Activate for:** original packshots, electronics, furniture, appliances, packaging, branded SKUs and reference-preserving composites.

Follow product-scene-compositing.md as the canonical workflow. This adds preservation diagnostics.

## Fidelity levels

- **F0 / exact source crop:** Original product RGB and orientation retained, only masking/cropping. No resize is strongest for pixel-level preservation.
- **F1 / visual identity preserved:** Uniform resize/resampling, soft alpha mask, placement. Source pixels are no longer identical.
- **F2 / modified asset:** Recolor, screen replacement, selective retouch, warping or generated missing geometry. Require explicit approval.

Never call F1/F2 "100% pixel-identical". Preserve screen images, logos, bezels, buttons, ports, stands, legs and physical ratios under strict matching.

## Before placement

Record source path/sha256, camera orientation, physical scale if known, invariants and must-preserve features, occlusions, matte quality, target size and fidelity level. Prefer official transparent packshots.

## Edge/mask checklist

Inspect at 100% over black, white and target scene. Verify transparent holes, handles, cables, anti-aliasing, glass, thin feet and supports. Correct color spill without corrupting source logos. Automatic GrabCut is only an approximate mask; hand repair complex edges.

## Composite physics

Start with compatible camera, believable support and coherent lighting. Add justified contact/cast shadows, ambient occlusion, reflection or foreground occlusion as separate layers. Blurred mask shadow is not a physically accurate render. When source is frontal, match scene projection; don't pretend a 2D warp creates a true new viewpoint. Multi-product scenes must preserve identities and plausible relative scales.

## Provenance and QA

Keep the original SHA-256, scene plate, separate shadow and product_SOURCE_LOCKED layer, any text layer, manifest and final preview. Compare with the original visually. Source hashing proves provenance, **not** rendered perfection.
