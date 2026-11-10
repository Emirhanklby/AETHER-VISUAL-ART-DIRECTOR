# Repository guidance for Codex contributors

- This repository is a **visual-first agent skill**, not a standalone image generator. Never claim an image has been generated or a product preserved unless artifacts were actually inspected.
- Keep SKILL.md as the discoverable entry point. Place detailed design, QA, camera, and compositing guidance under references/ and link it from SKILL.md.
- Preserve the rule: **Generate the world. Preserve the product.** Source RGB pixels and important product details should not be changed without a user-approved exception.
- Use the example inputs under examples/ and tests under tests/ when changing scripts/aether_visual.py.
- Before proposing a release, run python -m pytest -q after installing dependencies. State test results accurately.
- Do not bundle unlicensed third-party photographs, proprietary font binaries, branded product assets, or personal credentials.
- Keep installation guidance aligned with current official ChatGPT/Codex documentation; availability differs by plan and runtime.
