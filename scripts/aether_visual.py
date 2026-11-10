#!/usr/bin/env python3
"""AETHER offline production helpers: deterministic compositing, exact PNG export and audits.

Requires Pillow. Optional OpenCV + numpy for GrabCut masking.
Does NOT generate images or guarantee that manual visual QA has passed.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any
from PIL import Image, ImageChops, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps

RESAMPLE = Image.Resampling.LANCZOS
WEIGHTS = {
    "brand_audience_fit": 20,
    "originality_visual_idea": 20,
    "hierarchy_negative_space": 20,
    "feasibility_product_fidelity": 20,
    "truth_copy_legibility": 10,
    "format_crop_safe_zones": 10,
}
BLOCKERS = {"invented_claim_or_price", "protected_reference_reproduction",
            "product_identity_compromised", "mandatory_copy_illegible"}

def load_image(path: str) -> Image.Image:
    with Image.open(path) as im:
        im.load()
        return im.convert("RGBA")

def out_path(path: str) -> Path:
    p = Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.suffix.lower() != ".png":
        raise ValueError("Raster export must be a .png path")
    return p

def json_save(path: str | Path, payload: dict[str, Any]) -> None:
    p = Path(path).expanduser()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while (data := f.read(1 << 20)):
            h.update(data)
    return h.hexdigest()

def color_rgba(value: str, alpha: int = 255) -> tuple[int, int, int, int]:
    c = ImageColor.getrgb(value)
    if len(c) == 4:
        return (c[0], c[1], c[2], alpha)
    return c + (alpha,)

def cutout(args: argparse.Namespace) -> dict[str, Any]:
    im = load_image(args.product)
    with Image.open(args.mask) as src_mask:
        if src_mask.size != im.size:
            raise ValueError("Mask dimensions must match original product image exactly")
        mask = src_mask.convert("L")
    im.putalpha(ImageChops.multiply(mask, im.getchannel("A")))
    im.save(out_path(args.output))
    return {"operation": "cutout", "output": args.output, "size": list(im.size),
            "product_sha256": hash_file(args.product), "mask_sha256": hash_file(args.mask),
            "note": "Original RGB channels unchanged; alpha modified. Inspect edges and holes at 100% zoom."}

def segment(args: argparse.Namespace) -> dict[str, Any]:
    try:
        import cv2
        import numpy as np
    except ImportError as exc:
        raise ValueError("Segmentation needs opencv-python and numpy; use a hand-edited grayscale mask instead") from exc
    im = load_image(args.product)
    w, h = im.size
    x, y, rw, rh = (int(x) for x in args.rect.split(","))
    if not (0 <= x < w and 0 <= y < h and rw > 1 and rh > 1 and x + rw < w and y + rh < h):
        raise ValueError("Rectangle must be inside image with background outside; x,y,width,height")
    src = cv2.cvtColor(np.array(im.convert("RGB")), cv2.COLOR_RGB2BGR)
    mask = np.zeros((h, w), np.uint8)
    bg = np.zeros((1, 65), np.float64)
    fg = np.zeros((1, 65), np.float64)
    cv2.grabCut(src, mask, (x, y, rw, rh), bg, fg, 5, cv2.GC_INIT_WITH_RECT)
    binary = np.where((mask == 2) | (mask == 0), 0, 255).astype("uint8")
    alpha = Image.fromarray(binary, mode="L")
    alpha.save(out_path(args.mask_out))
    im.putalpha(ImageChops.multiply(im.getchannel("A"), alpha))
    im.save(out_path(args.output))
    return {"operation": "segment", "product_sha256": hash_file(args.product),
            "mask": args.mask_out, "cutout": args.output, "size": [w, h],
            "warning": "GrabCut makes only an approximate mask. Inspect/repair fine edges and transparent areas."}

def composite(args: argparse.Namespace) -> dict[str, Any]:
    scene = load_image(args.scene)
    product = load_image(args.product)
    bbox = product.getchannel("A").getbbox()
    if bbox is None:
        raise ValueError("Product alpha is entirely transparent")
    product = product.crop(bbox)
    orig_size = product.size
    if args.width is not None:
        if args.width <= 0:
            raise ValueError("--width must be positive")
        h2 = max(1, round(product.height * args.width / product.width))
        product = product.resize((args.width, h2), RESAMPLE)
    x, y = int(args.x), int(args.y)
    shadow = Image.new("RGBA", scene.size, (0, 0, 0, 0))
    if args.shadow_opacity > 0:
        mask = Image.new("L", scene.size, 0)
        mask.paste(product.getchannel("A"), (x + args.shadow_dx, y + args.shadow_dy))
        mask = mask.filter(ImageFilter.GaussianBlur(args.shadow_blur))
        mask = mask.point(lambda a: round(a * args.shadow_opacity))
        shadow = Image.new("RGBA", scene.size, color_rgba(args.shadow_color))
        shadow.putalpha(mask)
    locked_product = Image.new("RGBA", scene.size, (0, 0, 0, 0))
    locked_product.alpha_composite(product, (x, y))
    out = Image.alpha_composite(scene, shadow)
    out = Image.alpha_composite(out, locked_product)
    if args.occlusion_layer:
        occlusion = load_image(args.occlusion_layer)
        if occlusion.size != scene.size:
            raise ValueError("Foreground occlusion layer must match scene pixels")
        out = Image.alpha_composite(out, occlusion)
    out.save(out_path(args.output))
    manifest: dict[str, Any] = {
        "operation": "composite", "output": args.output,
        "scene": args.scene, "scene_sha256": hash_file(args.scene),
        "product_cutout": args.product, "product_cutout_sha256": hash_file(args.product),
        "original_product_visible_bbox": list(bbox), "original_crop_size": list(orig_size),
        "placed_size": list(product.size), "xy": [x, y], "canvas": list(scene.size),
        "resampled": product.size != orig_size,
        "shadow_parameters": {"opacity": args.shadow_opacity, "blur": args.shadow_blur,
                              "offset": [args.shadow_dx, args.shadow_dy]},
        "occlusion_layer": args.occlusion_layer,
        "manual_review_required": ["scene plausibility", "mask edges", "light direction",
            "product identity", "physical support", "text and claims", "final visible composition"]}
    if args.project_dir:
        p = Path(args.project_dir)
        p.mkdir(parents=True, exist_ok=True)
        scene.save(p / "00_scene_plate.png")
        shadow.save(p / "20_separate_shadow.png")
        locked_product.save(p / "40_product_SOURCE_LOCKED.png")
        if args.occlusion_layer:
            occlusion.save(p / "50_foreground_occlusion.png")
        out.save(p / "90_preview.png")
        json_save(p / "composition.json", manifest)
    return manifest

def parse_size(value: str) -> tuple[int, int]:
    parts = value.lower().split("x")
    if len(parts) != 2:
        raise ValueError("--size uses WIDTHxHEIGHT e.g. 1080x1350")
    w, h = int(parts[0]), int(parts[1])
    if w <= 0 or h <= 0 or w > 15000 or h > 15000:
        raise ValueError("Image dimensions must be positive and <= 15000")
    return w, h

def grid_preview(im: Image.Image, out: str) -> list[int]:
    w, h = im.size
    cropw = round(h * 3 / 4)
    if cropw > w:
        raise ValueError("Input too narrow for a centered 3:4 grid crop")
    left = (w - cropw) // 2
    im.crop((left, 0, left + cropw, h)).save(out_path(out))
    return [left, 0, left + cropw, h]

def export(args: argparse.Namespace) -> dict[str, Any]:
    im = load_image(args.input)
    width, height = parse_size(args.size)
    source_w, source_h = im.size
    if args.fit == "contain":
        scaled = ImageOps.contain(im, (width, height), method=RESAMPLE)
        canvas = Image.new("RGBA", (width, height)) if args.background == "transparent" else Image.new("RGBA", (width, height), color_rgba(args.background))
        dx, dy = (width - scaled.width) // 2, (height - scaled.height) // 2
        canvas.alpha_composite(scaled, (dx, dy))
    else:
        canvas = ImageOps.fit(im, (width, height), method=RESAMPLE,
                              centering=(args.center_x, args.center_y))
    canvas.save(out_path(args.output))
    report: dict[str, Any] = {"operation": "export", "input_size": [source_w, source_h],
        "output_size": [width, height], "output": args.output, "fit": args.fit,
        "upscaled_by_interpolation": width > source_w or height > source_h,
        "manual_review_required": "Inspect important content. This is NOT AI super-resolution."}
    if args.grid_preview:
        report["grid_crop_xyxy"] = grid_preview(canvas, args.grid_preview)
        report["grid_preview"] = args.grid_preview
    return report

def wrapping(text: str, draw: ImageDraw.ImageDraw, font: ImageFont.FreeTypeFont,
             max_width: int | None) -> list[str]:
    lines = []
    for line in text.split("\n"):
        if not max_width or draw.textlength(line, font=font) <= max_width:
            lines.append(line)
            continue
        current = ""
        for token in line.split(" "):
            candidate = f"{current} {token}".strip()
            if current and draw.textlength(candidate, font=font) > max_width:
                lines.append(current)
                current = token
            else:
                current = candidate
        lines.append(current)
    return lines

def typeset(args: argparse.Namespace) -> dict[str, Any]:
    base = load_image(args.input)
    layout = json.loads(Path(args.layout).read_text(encoding="utf-8"))
    elements = layout.get("elements", [])
    if not elements:
        raise ValueError("Layout must contain nonempty 'elements' array")
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    rects = []
    for item in elements:
        font_file = Path(item["font_file"])
        if not font_file.is_file():
            raise ValueError(f"Font file missing: {font_file}. No silent font substitution permitted.")
        size = int(item["font_size"])
        if size <= 0:
            raise ValueError("font_size must be positive")
        font = ImageFont.truetype(str(font_file), size)
        x, y = int(item["x"]), int(item["y"])
        fill = item.get("fill", "#FFFFFF")
        spacing = float(item.get("line_spacing", 1.15))
        if spacing <= 0:
            raise ValueError("line_spacing must be positive")
        lines = wrapping(str(item["text"]), draw, font, item.get("max_width"))
        height = max(1, math.ceil(size * spacing))
        rect = [x, y, x, y]
        for i, line in enumerate(lines):
            ty = y + i * height
            draw.text((x, ty), line, font=font, fill=fill, anchor="lt")
            b = draw.textbbox((x, ty), line or " ", font=font, anchor="lt")
            rect[0] = min(rect[0], b[0]); rect[1] = min(rect[1], b[1])
            rect[2] = max(rect[2], b[2]); rect[3] = max(rect[3], b[3])
        rects.append({"label": item.get("label", item["text"][:24]), "bbox": rect,
                      "text": item["text"], "font_file": str(font_file), "lines": lines})
    final = Image.alpha_composite(base, overlay)
    final.save(out_path(args.output))
    if args.overlay:
        overlay.save(out_path(args.overlay))
    report = {"operation": "typeset", "output": args.output, "size": list(base.size),
              "text_boxes": rects,
              "note": "Render from supplied fonts. Review actual visible text and contrast manually."}
    if args.report:
        json_save(args.report, report)
    return report

def safe_rect(w: int, h: int, platform: str) -> tuple[int, int, int, int] | None:
    if platform == "instagram-feed":
        if (w, h) == (1080, 1080):
            return (135, 60, 945, 1020)
        if (w, h) == (1080, 1350):
            return (60, 60, 1020, 1290)
        raise ValueError("Known Instagram Feed safe rectangles apply ONLY to 1080x1080 and 1080x1350")
    return None

def audit(args: argparse.Namespace) -> dict[str, Any]:
    im = load_image(args.input)
    w, h = im.size
    problems = []
    checks: list[dict[str, Any]] = []
    if args.size:
        expected = parse_size(args.size)
        passed = (w, h) == expected
        checks.append({"test": "exact_canvas_dimensions", "passed": passed,
                       "expected": list(expected), "actual": [w, h]})
        if not passed:
            problems.append("canvas dimensions")
    rectangle = safe_rect(w, h, args.platform)
    if args.boxes:
        boxes_json = json.loads(Path(args.boxes).read_text(encoding="utf-8"))
        boxes = boxes_json.get("boxes", boxes_json.get("text_boxes", []))
        if not isinstance(boxes, list):
            raise ValueError("--boxes JSON must contain array 'boxes' or 'text_boxes'")
        for box in boxes:
            b = box["bbox"]
            if len(b) != 4:
                raise ValueError("Each bbox must be [left,top,right,bottom]")
            inside = (0 <= b[0] < b[2] <= w and 0 <= b[1] < b[3] <= h)
            if rectangle is not None:
                inside = inside and (b[0] >= rectangle[0] and b[1] >= rectangle[1] and
                                      b[2] <= rectangle[2] and b[3] <= rectangle[3])
            checks.append({"test": "critical_content_bbox", "label": box.get("label", "unnamed"),
                           "passed": inside, "bbox": b})
            if not inside:
                problems.append("critical safe zone: " + box.get("label", "unnamed"))
    result: dict[str, Any] = {"operation": "audit", "input": args.input,
        "input_sha256": hash_file(args.input), "size": [w, h], "platform": args.platform,
        "safe_rectangle": list(rectangle) if rectangle else None, "checks": checks,
        "machine_checks_passed": not problems, "problems": problems,
        "unverified_manual_checks": ["exact visible spelling", "visual hierarchy", "brand color fidelity",
            "font verification", "contrast against photographic texture", "realistic lighting and contact",
            "creative originality", "source-product comparison", "thumbnail readability"]}
    if not args.boxes and args.platform != "none":
        result["warning"] = "No content rectangles provided: safe-zone compliance NOT verified"
    if args.report:
        json_save(args.report, result)
    return result

def evaluate(args: argparse.Namespace) -> dict[str, Any]:
    spec = json.loads(Path(args.input).read_text(encoding="utf-8"))
    concepts = spec.get("concepts", [])
    if not isinstance(concepts, list) or len(concepts) < 2:
        raise ValueError("Concept evaluation requires at least two distinct directions")
    scored = []
    for c in concepts:
        name = str(c.get("name", "")).strip()
        if not name:
            raise ValueError("Each concept needs a name")
        ratings = c.get("ratings", {})
        evidence = c.get("evidence", {})
        total = 0.0
        for dimension, weight in WEIGHTS.items():
            if dimension not in ratings or dimension not in evidence:
                raise ValueError(f"{name}: missing {dimension} score or evidence")
            rating = ratings[dimension]
            if not isinstance(rating, (int, float)) or isinstance(rating, bool) or not (0 <= rating <= 5):
                raise ValueError(f"{name}: rating for {dimension} must be in [0,5]")
            if not str(evidence[dimension]).strip():
                raise ValueError(f"{name}: evidence for {dimension} must be explained")
            total += weight * rating / 5
        flags = c.get("red_flags", [])
        unknown = set(flags) - BLOCKERS
        if unknown:
            raise ValueError(f"Unknown blockers: {', '.join(sorted(unknown))}")
        blocked = bool(flags)
        scored.append({"name": name, "score": round(total, 1), "blocked": blocked,
                       "red_flags": flags, "rationale": c.get("rationale", ""), "evidence": evidence})
    scored.sort(key=lambda e: (not e["blocked"], e["score"]), reverse=True)
    valid = [c for c in scored if not c["blocked"]]
    best = valid[0] if valid else None
    decision = ("proceed" if best and best["score"] >= 80 else
                "revise_best_concept" if best and best["score"] >= 65 else "rethink_concepts")
    result = {"operation": "concept_evaluation", "assessment": "provisional, pre-render human-assigned scores",
        "weights": WEIGHTS, "ranked_concepts": scored, "selected": best["name"] if best else None,
        "decision": decision,
        "note": "Scores are only as reliable as supplied evidence; run visual QA after production."}
    if args.report:
        json_save(args.report, result)
    return result

def cli() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    subs = p.add_subparsers(dest="command", required=True)
    def make(name: str, summary: str):
        return subs.add_parser(name, help=summary)
    q = make("inspect", "Inspect metadata including alpha bbox and dimensions")
    q.add_argument("--input", required=True)
    q = make("cutout", "Apply grayscale mask while retaining source product RGB")
    q.add_argument("--product", required=True); q.add_argument("--mask", required=True); q.add_argument("--output", required=True)
    q = make("segment", "Approximate product mask using OpenCV GrabCut; manual review required")
    q.add_argument("--product", required=True); q.add_argument("--rect", required=True, help="x,y,width,height")
    q.add_argument("--mask-out", required=True); q.add_argument("--output", required=True)
    q = make("composite", "Original product alpha over scene, separated layers")
    for name in ["scene", "product", "output"]: q.add_argument("--"+name, required=True)
    for name in ["x", "y"]: q.add_argument("--"+name, required=True, type=int)
    q.add_argument("--width", type=int, help="Uniform target width; omitted preserves native pixels")
    q.add_argument("--shadow-opacity", type=float, default=0, help="0..1, default 0")
    q.add_argument("--shadow-blur", type=float, default=20)
    q.add_argument("--shadow-dx", type=int, default=8); q.add_argument("--shadow-dy", type=int, default=12)
    q.add_argument("--shadow-color", default="#000000")
    q.add_argument("--occlusion-layer"); q.add_argument("--project-dir")
    q = make("export", "Exact-pixel PNG export with contain/cover and grid preview")
    q.add_argument("--input", required=True);q.add_argument("--output", required=True);q.add_argument("--size", required=True)
    q.add_argument("--fit", choices=["contain", "cover"], default="contain")
    q.add_argument("--background", default="transparent")
    q.add_argument("--center-x", type=float, default=0.5);q.add_argument("--center-y", type=float, default=0.5)
    q.add_argument("--grid-preview")
    q = make("typeset", "Overlay exact copy using explicitly supplied font files")
    q.add_argument("--input", required=True);q.add_argument("--layout", required=True);q.add_argument("--output", required=True)
    q.add_argument("--overlay");q.add_argument("--report")
    q = make("audit", "Machine-check exact dimensions and declared safe-zone boxes")
    q.add_argument("--input", required=True);q.add_argument("--size")
    q.add_argument("--platform", choices=["none", "instagram-feed"], default="none")
    q.add_argument("--boxes", help="JSON file with critical content bounding boxes")
    q.add_argument("--report")
    q = make("evaluate", "Score at least 2 creative directions using 6 weighted criteria")
    q.add_argument("--input", required=True);q.add_argument("--report")
    return p

def main() -> int:
    parser = cli()
    args = parser.parse_args()
    try:
        if args.command == "inspect":
            with Image.open(args.input) as im:
                im.load()
                result = {"operation": "inspect", "file": args.input,
                    "size": list(im.size), "mode": im.mode, "format": im.format,
                    "sha256": hash_file(args.input),
                    "alpha_bbox": list(im.getchannel("A").getbbox()) if "A" in im.getbands() and im.getchannel("A").getbbox() else None}
        else:
            if args.command == "composite":
                if not (0 <= args.shadow_opacity <= 1 and args.shadow_blur >= 0):
                    raise ValueError("Shadow opacity must be 0..1 and blur >=0")
            result = globals()[args.command](args)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.command == "audit" and not result["machine_checks_passed"]:
            return 2
        return 0
    except (OSError, ValueError, KeyError, json.JSONDecodeError) as exc:
        parser.exit(2, f"AETHER error: {exc}\n")

if __name__ == "__main__":
    raise SystemExit(main())
