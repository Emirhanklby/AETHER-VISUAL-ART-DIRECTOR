# Codex kurulumu

Codex skill'i bir klasör ve içindeki SKILL.md dosyasıyla tanır. Proje düzeyinde klasör .agents/skills/, kullanıcı düzeyinde ~/.agents/skills/ olarak kullanılır.

## Her proje için (macOS / Linux)

~~~bash
mkdir -p ~/.agents/skills
git clone https://github.com/Emirhanklby/AETHER-VISUAL-ART-DIRECTOR.git ~/.agents/skills/aether-visual-art-director
~~~

Windows PowerShell:

~~~powershell
New-Item -ItemType Directory -Force "$HOME/.agents/skills" | Out-Null
git clone https://github.com/Emirhanklby/AETHER-VISUAL-ART-DIRECTOR.git "$HOME/.agents/skills/aether-visual-art-director"
~~~

## Yalnızca açık proje için

~~~bash
mkdir -p .agents/skills
git clone https://github.com/Emirhanklby/AETHER-VISUAL-ART-DIRECTOR.git .agents/skills/aether-visual-art-director
~~~

Depo private ise klonlamadan önce GitHub'a giriş yapılmalıdır.

## Python yardımcıları

~~~bash
python -m pip install -r requirements.txt
python scripts/aether_visual.py --help
python scripts/aether_visual.py evaluate --input examples/concepts.json
~~~

Opsiyonel maskeleme: python -m pip install opencv-python numpy. Testler: python -m pip install pytest && python -m pytest -q.

## Kullanım

> Use $aether-visual-art-director. Review this product photo, propose three premium creative directions, select one using Concept Evaluation, preserve exact product details and prepare the compositing plan for a 1080×1350 social ad.

Skill görünmüyorsa SKILL.md dosyasının skill klasörünün kökünde bulunduğunu ve çalışma dizinini kontrol edin. Codex ortamında görsel üretme aracı yoksa fotoğraf üretimi yapılamaz; ancak prompt ve kompozit işlemleri hazırlanabilir.
