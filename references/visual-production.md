# AETHER Visual Production — reproducible production guide

AETHER's art direction defines the outcome. The local script can produce **source-preserving PNG composites** and mechanical QC when files are available. Requires Python 3.10+ and Pillow, optionally OpenCV/numpy for rough GrabCut. It does not include Photoshop, image-generation models or licensed font files.

## Choose the correct route

| Task | Method |
|---|---|
| Generate a new photographic scene | Use an accessible image-generation tool. Python script cannot invent new images. |
| Insert an existing authentic product | Generate/source an **empty scene plate**; mask original; composite approved original RGBA on top. |
| Transparent product asset already exists | Inspect dimensions/alpha then composite; do not re-segment. |
| Product photo has an opaque background | Supply hand-edited grayscale mask, or use segment as a rough start and repair manually. |
| Exact text | Generate text-free backdrop, then typeset using available approved font file. |
| Multiple products | Make independent approved alpha assets and composite in clear, physically plausible depth order. |
| Story/Reels or alternate formats | Recompose for each actual format; export can resize/crop but is not art direction. |
| 2K/4K | Export native dimensions where possible; LANCZOS enlargement is interpolation, **not** AI super-resolution. |

## Source-lock process

0. Preserve original image, record source SHA-256, RGB colors, camera viewpoint, logo, text and protected geometry.
1. Generate or supply an EMPTY scene plate with perspective and light designed around the original packshot.
2. If source lacks alpha, use a reviewed mask:

~~~bash
python scripts/aether_visual.py cutout --product product-original.png --mask mask.png --output product-cutout.png
~~~

Optional rough auto-mask, requires OpenCV and numpy. Always hand-inspect/repair:

~~~bash
python scripts/aether_visual.py segment --product product-original.png --rect 60,30,740,820 --mask-out rough-mask.png --output rough-cutout.png
~~~

3. Composite the source-locked product. Omit width parameter to preserve native RGB pixels. Default cast shadow is disabled: shadow realism requires editorial judgment.

~~~bash
python scripts/aether_visual.py composite --scene scene.png --product product-cutout.png --x 320 --y 370 --output ad-no-type.png --project-dir project-layers
~~~

Optional proportional resize: --width 460. Optional rough shadow: --shadow-opacity 0.18 --shadow-blur 20 --shadow-dx 10 --shadow-dy 16. Optional foreground occlusion: --occlusion-layer foreground.png. Project folder stores separate PNG assets and composition.json, **not** an editable PSD.

4. Prepare text-layout JSON with real approved font paths:

~~~json
{
  "elements": [
    {"label":"headline","text":"Kasım Fırsatları","x":94,"y":92,"font_file":"/absolute/path/to/approved-font.ttf","font_size":74,"fill":"#FFFFFF","max_width":780},
    {"label":"dates","text":"13–27 Kasım","x":94,"y":202,"font_file":"/absolute/path/to/approved-font.ttf","font_size":32,"fill":"#FFFFFF"}
  ]
}
~~~

~~~bash
python scripts/aether_visual.py typeset --input ad-no-type.png --layout type-layout.json --output ad-final.png --overlay text-layer.png --report type-bounds.json
~~~

5. Export exact placements. Inspect all variants; contain may leave bars, cover can crop important elements:

~~~bash
python scripts/aether_visual.py export --input ad-final.png --size 1080x1350 --fit contain --output feed-4x5.png --grid-preview grid-3x4.png
python scripts/aether_visual.py export --input ad-final.png --size 1080x1080 --fit cover --output feed-square.png --grid-preview square-grid-3x4.png
python scripts/aether_visual.py export --input ad-final.png --size 1080x1920 --fit contain --output story.png
~~~

6. Audit actual pixel size and declared critical text/visual bounding boxes:

~~~bash
python scripts/aether_visual.py audit --input ad-final.png --size 1080x1350 --platform instagram-feed --boxes type-bounds.json --report ad-audit.json
~~~

Bounding boxes can be a JSON object with "boxes":[{"label":"logo","bbox":[100,100,300,180]}] or the text_boxes from typeset report. Only declared boxes are checked. If boxes are missing, safe-zone compliance is **not** verified. Machine QA does **not** verify visible text spelling, photographic plausibility, brand colors, actual WCAG contrast, copyright ownership or product identity. Review full-resolution rendered PNG.

## Deliverables

Exact-size PNG, optional original source cutout and empty background plate, independent shadow/source-locked-product/text overlays, composition manifest and SHA-256, crop previews and a machine QA report **plus** a separate manual QA verdict. Never call a generated lookalike an original product composite.

Keep verified reference provenance. Do not use unlicensed third-party photos or protected designs as reusable final assets.
