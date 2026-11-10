"""Tests use synthetic assets; no external network or third-party photography."""
import json
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "aether_visual.py"

def run(*args, expected=0):
    p = subprocess.run([sys.executable, str(SCRIPT), *map(str,args)], capture_output=True,text=True)
    assert p.returncode == expected, f"OUT: {p.stdout}\nERR: {p.stderr}"
    return json.loads(p.stdout) if p.stdout else None

def setup_assets(tmp_path):
    product = Image.new("RGBA", (100, 120), (220, 30, 40, 255))
    prod = tmp_path/"product.png";product.save(prod)
    scene = Image.new("RGBA",(1080,1350),(15,20,30,255))
    scene_path=tmp_path/"scene.png";scene.save(scene_path)
    mask=Image.new("L",(100,120),0)
    ImageDraw.Draw(mask).rectangle((20,10,79,109),fill=255)
    mp=tmp_path/"mask.png";mask.save(mp)
    return prod,scene_path,mp

def test_cutout_keeps_source_rgb(tmp_path):
    product,scene,mask=setup_assets(tmp_path)
    out=tmp_path/"cutout.png"
    run("cutout","--product",product,"--mask",mask,"--output",out)
    with Image.open(out) as f:
        im=f.convert("RGBA")
        assert im.getpixel((30,30))==(220,30,40,255)
        assert im.getpixel((0,0))==(220,30,40,0)

def test_composite_layers_and_geometry(tmp_path):
    product,scene,mask=setup_assets(tmp_path)
    cut=tmp_path/"cut.png"
    run("cutout","--product",product,"--mask",mask,"--output",cut)
    out=tmp_path/"ad.png"; project=tmp_path/"layers"
    info=run("composite","--scene",scene,"--product",cut,"--x","300","--y","400",
             "--output",out,"--project-dir",project)
    assert info["resampled"] is False
    assert (project/"00_scene_plate.png").exists()
    assert (project/"40_product_SOURCE_LOCKED.png").exists()
    assert (project/"composition.json").exists()
    with Image.open(out) as im:
        assert im.size==(1080,1350)
        assert im.getpixel((330,420))[:3]==(220,30,40)
        assert im.getpixel((30,30))[:3]==(15,20,30)

def test_export_grid_preview_and_audit(tmp_path):
    product,scene,mask=setup_assets(tmp_path)
    out=tmp_path/"square.png";preview=tmp_path/"grid.png"
    info=run("export","--input",scene,"--size","1080x1080","--fit","cover",
             "--output",out,"--grid-preview",preview)
    assert info["output_size"]==[1080,1080]
    with Image.open(preview) as im:
        assert im.size==(810,1080)
    boxes=tmp_path/"boxes.json"
    boxes.write_text(json.dumps({"boxes":[{"label":"headline","bbox":[200,90,700,220]}]}))
    assert run("audit","--input",out,"--size","1080x1080","--platform","instagram-feed",
               "--boxes",boxes)["machine_checks_passed"]
    boxes.write_text(json.dumps({"boxes":[{"label":"headline","bbox":[20,90,700,220]}]}))
    assert run("audit","--input",out,"--size","1080x1080","--platform","instagram-feed",
               "--boxes",boxes,expected=2)["machine_checks_passed"] is False

def test_evaluator_with_example():
    c=Path(__file__).resolve().parents[1]/"examples"/"concepts.json"
    result=run("evaluate","--input",c)
    assert result["selected"]=="Architectural Quiet"
    assert result["decision"]=="proceed"
    assert result["ranked_concepts"][0]["score"]>=80

def test_typeset_with_real_font_or_skip(tmp_path):
    candidates=[p for p in Path("/usr/share/fonts").rglob("*.ttf") if p.name in {"DejaVuSans.ttf", "LiberationSans-Regular.ttf"}]
    if not candidates:return  # An outline font is needed; fixed-size emoji fonts reject arbitrary px sizes
    product,scene,mask=setup_assets(tmp_path)
    layout=tmp_path/"type.json"
    layout.write_text(json.dumps({"elements":[
        {"label":"headline","text":"Kasım Fırsatları","x":150,"y":100,
         "font_file":str(candidates[0]),"font_size":60,"fill":"#FFFFFF"}]}),encoding="utf8")
    out=tmp_path/"typed.png";report=tmp_path/"type_report.json"
    result=run("typeset","--input",scene,"--layout",layout,"--output",out,"--report",report)
    assert out.exists() and report.exists()
    assert result["text_boxes"][0]["text"]=="Kasım Fırsatları"
