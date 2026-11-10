# AETHER — Product Scene Art Direction & Compositing playbook

## Mission

Create sophisticated, original product advertising scenes **without redrawing a real supplied product**. The highest-quality strategy is to generate/source the world around the item and composite the genuine product photo as a separate layer. A visually similar AI-rendered replacement does **not** satisfy strict fidelity.

## 1. Choose the route based on the source asset

| Source condition | Preferred method | Limitation / decision |
| --- | --- | --- |
| Official transparent PNG/PSD packshot | Preserve alpha and composite directly | Check shadows/white fringing embedded in the source |
| High-resolution photo with clean background | Extract mask and preserve foreground pixels | Inspect edges, fine details, transparent parts; never assume cutout is perfect |
| Photo with complex occlusions or reflections | Retouch/extract with careful masks, optionally manual correction | Recreate environment behind masked edges, not the product itself |
| Blurry, heavily compressed, strongly angled, partially hidden product | Use best faithful source; constrain design and camera to suit it | Strict detail fidelity may be impossible; request better photo only if needed |
| No product image / no rights to source | Produce concept/prompt/background only or use user-approved asset | Do not invent and claim exact preservation |

## 2. Creative scene families

- **Architectural interior:** boutique living room, understated gallery, designer kitchen, luxury hotel, warm modern workspace. Product should be realistically sized and plausibly supported/installed, with camera/viewpoint compatible with the original photo.
- **Sculptural studio:** travertine plinth, matte metal, layered paper, polished concrete, restrained reflective surfaces. One tactile material contrast beats many decorative forms.
- **Conceptual advertising:** surreal landscape, floating architectural volumes, mirrored floor, visual metaphor for speed/clarity/lightness. The **world** may be fantastical; the **product identity** remains unchanged.
- **Minimal hero:** neutral cyclorama or one carefully lit plane; strong scale and silhouette, plenty of space for ad typography.

Make one concept the clear winner. Specify a composition map: hero center in approximate canvas coordinates, empty copy zone, eye line, floor/wall intersection, shadow footprint, crop and safe region. Do not assume a product can be rotated to a completely different view through a 2D composite.

## 3. Scene-plate generation: generate an empty world

Define the background independently of the product. Prompt the model to create a high-quality **unoccupied** photographic environment with the correct vacant area and grounding surface. Do not ask it to draw the supplied product inside the background; when a temporary placeholder is unavoidable, remove/replace it before delivery.

**Background-plate prompt template (adapt per brief):**

> Create an empty photorealistic premium advertising environment, [FORMAT, PX, ASPECT]. Art direction: [AUDIENCE/MOOD, MATERIALS, ARCHITECTURE]. Reserve an unobstructed product-placement region approximately [POSITION / SCALE] for a separately composited original product photograph; leave a physically plausible support surface and accurate floor/wall intersection there. Camera: [VIEWPOINT, LENS FEEL, HORIZON, HEIGHT]. Lighting: [DIRECTION, SOFTNESS, COLOR TEMPERATURE] consistent with the product source. Composition: [NEGATIVE SPACE FOR TYPOGRAPHY]. Natural texture, restrained highlights, believable shadows in the environment. **No product, no stand-in object, no text, no labels, no logos, no watermarks, no extra hero props**. Keep geometry and surfaces believable and the placement region clear.

The scene plate alone may intentionally have no product shadow; create product-specific shadows after product size and position are fixed. If the model accidentally adds an imaginary product, repair the empty plate rather than layering the original directly on top of a double.

## 4. Product isolation (non-destructive)

1. Keep `product_original` immutable and retain provenance to the uploaded/approved source.
2. Produce an `alpha_mask` for the physical silhouette: preserve holes, thin supports, cords, transparent glass, reflections and shadows only where they actually belong. Compare against original at 100% zoom.
3. Store the clean cutout as `product_cutout`, on its own layer; avoid artificially painted edge highlights, over-feathering or erasing meaningful detail.
4. Match placement mainly by translation and uniform scale. Never stretch width/height independently. Avoid strong perspective transform or rotation that makes the original view inconsistent. Resizing necessarily resamples pixels; do **not** claim binary pixel identity after resize.
5. If original product has a baked-in background/reflection/shadow that prevents clean extraction, acknowledge it and design around it or ask for a cleaner source when essential. Do not hallucinate hidden product geometry.

## 5. Photographic integration

- **Geometry:** Align product base/support with the actual floor, table, wall mount or plinth. Check horizon, vanishing points, camera height, object scale and perspective; prefer generating an environment to match the product photo's camera angle.
- **Light:** Match source highlight/shadow direction, softness and color temperature; for strict fidelity adjust the plate and environmental layers instead of recoloring the product itself.
- **Contact shadow:** Small, dark, soft-to-firm shadow at actual contact points; never float a product unless the campaign intentionally shows a levitating object.
- **Cast shadow:** Follow source light direction, surface slope and object scale; keep it on a separate layer. Soften with distance and material cues. Avoid a generic blurred black oval disconnected from the product.
- **Ambient occlusion:** Subtle darkening near contacts/corners/behind the product, not a giant black halo.
- **Reflection:** Only if the support material warrants one. Reflection must follow product silhouette, viewpoint and surface roughness, with appropriate blur and falloff; should not duplicate the product as a second item.
- **Foreground occlusion:** When the product is behind a real object or built-in edge, composite that foreground edge on top with a separate mask. Do not repaint protected product internals.
- **Edge fidelity:** Prevent white/black halos, mismatched sharpness, oversharpening, conspicuous cutout outlines, and inconsistent motion/depth blur.
- **Depth/grade:** Prefer limited grades to environment. If a global grade touches the source product, disclose that exact per-pixel preservation no longer holds.

## 6. Delivery layers / file practices

Use a layered editor (Photoshop, Photopea, Affinity, Figma where suitable, or code/Pillow/OpenCV) if present. Suggested layers:

```text
00__scene_plate (generated/sourced environment)
10__distant_atmosphere
20__cast_shadow
30__contact_shadow_and_AO
40__product_cutout__SOURCE_LOCKED
50__foreground_occlusions
60__reflections_or_lightwrap (if justified)
70__editable_headline_price_logo
80__optional_environment_only_grade
```

Retain a master layered project where the workflow permits it. Export requested PNG/JPEG at exact canvas size plus original cutout (optional). If an exported result flattens layers, do not claim it is editable. Preserve important content in Instagram safe zones as described in `platform-safe-zones.md`.

## 7. Final QA / stop conditions

Check the final actual pixels, not only the prompt:

- [ ] Product shape, proportions, model, color, stand, ports, logo, screen content and surface details match source.
- [ ] Product came from the genuine source cutout, **not a generated approximation**.
- [ ] Alpha edge looks natural on light and dark areas; no mask holes or fringe.
- [ ] Perspective, contact point, true-to-scene scale and support surface are plausible.
- [ ] Light direction, cast/contact shadows, reflection and occlusion are coherent.
- [ ] No unwanted duplicate product in the scene plate; no invented functionality.
- [ ] One visual hero, strong negative space, restrained palette, correct typography and message.
- [ ] Exact output dimensions and platform crop safe zone; critical product features visible.
- [ ] Final exported image reopened and inspected; mention anything unverified.

**Stop or disclose:** If compositing tools, source asset, mask quality or viewpoint make strict preservation impossible, do **not** describe a one-pass regenerated visual as a flawless composite. Deliver the verified parts (e.g. empty environment, cutout, or production-ready 2-stage prompt) and identify what remains unverified.

## 8. Examples of art-direction decisions

**TV in an interior:** Select a clean living room whose camera faces the television straight on if the product source is frontal; preserve the exact screen image and both legs/stand. Create the room behind the locked TV cutout, integrate realistic wall/furniture shadows, and avoid invented bezel or mounting details. If a wall mount would require hiding the original stands, choose a console/stand scene instead or get explicit approval to alter the composition.

**Small appliance in a premium kitchen:** Keep buttons, materials and logo untouched; construct a kitchen counter at an appropriate camera height and introduce a contact shadow/reflection compatible with that surface. Do not let generated cabinet lines cut through the appliance.

**Conceptual floating-product advertisement:** For deliberate levitation, omit contact shadow but use a physically coherent distant cast shadow and supporting visual language. Keep the product unchanged and let surrounding floating shapes/environment carry the surreal idea.