# Visual Reference Mining — operating playbook

This file expands the research step of the main skill. The research step exists to prevent generic template-style results. It is **not** a requirement to copy any one design or to fabricate a reference survey when web access is unavailable.

## 1. Create the search brief

Before searching, write:
- Audience and desired perception (e.g. design-literate, contemporary, trustworthy, futuristic but restrained).
- Channel and format (e.g. 1080x1350 feed campaign, short thumbnail viewing distance).
- Brand or product invariants; mandatory information and available logo/product assets.
- Three to five **style-oriented** search directions, broad enough to uncover unusual but relevant design solutions.

**Examples of style-oriented queries** (adapt to the brief):
- `site:behance.net luxury tech editorial campaign art direction negative space`
- `site:behance.net swiss minimal typography product poster studio`
- `site:pinterest.com asymmetric editorial advertising layout muted palette`
- `site:behance.net conceptual product photography advertising design`
- `site:fontsinuse.com high contrast grotesk editorial advertising`
- `site:are.na sculptural still life graphic design composition`

Avoid topic-only searches (`telephone advertising`, `discount poster`) as the primary strategy. They often surface generic examples instead of strong design systems.

## 2. Inspect real, attributable references proportionally

Search Behance, Pinterest, Dribbble, Awwwards, Are.na, Designspiration, Fonts in Use, and Brand New / UnderConsideration as relevant to the brief. Prefer original case studies and credited designers; check that a Pinterest pin's linked image is genuinely attributable when possible. For deep research requested by the user, aim for 15–30 unique references. For an ordinary single visual, inspect a smaller useful set and proceed; do not delay production to meet a quota.

Tool fallback order:
1. If actually available, search with `bd:search_engine` and targeted `site:` operators; use `bd:scrape_as_markdown` or `bd:scrape_as_html` to inspect publicly accessible pages or boards.
2. Otherwise use available web search and site-navigation/browser capabilities to inspect pages and visible content.
3. If pages cannot be accessed, rely on what is verifiably visible and record the limitation. Never guess creator names, claim pages were scraped, or simulate a large reference set.

Do not bypass restrictions or scrape private content. Cite reference URLs; do not download or reuse protected creative assets as ready-to-use deliverables unless authorized.

## 3. Scratchpad template

Create a working note titled **Visual Research** (a local Markdown file, project note, or ordinary response notes, depending on what is available). Use this structure:

```md
# Visual Research

## Brief & aesthetic target
Audience:
Feeling:
Format:
Brand constraints:
Search directions:

## References (actual inspected set)
| # | Source URL | Creator / project | Principle to learn | Role | Relevant? |
|---|------------|-------------------|--------------------|------|-----------|
| 01 | https://... | ... | Vast quiet upper-right zone and tight subject crop | Composition | Yes |
| 02 | https://... | ... | Warm charcoal + muted jade, with narrow accent use | Palette | Yes |
| 03 | https://... | ... | Large neutral grotesk with very small utility captions | Typography | Yes |

## Pattern analysis
- Palette: [color combinations], observed in [count of N verified refs]
- Typography: [families, scale contrast, spacing], observed in [...]
- Composition: [grid, asymmetry, negative-space ratio], observed in [...]
- Texture/lighting: [grain, shadows, reflections, treatments], observed in [...]
- Exceptions or contrary examples: [...]
- Patterns to *avoid*: [overused/noisy tropes]

## Design Direction
For [audience], combine [A URL]'s broad spatial principle with [B URL]'s color relationship and [C URL]'s typographic rhythm. This works because [rationale]. Distinct new concept: [idea]. Preserve [brand/product constraints]. Avoid [cliches].

## Source provenance and originality check
- Reference A influenced: [high-level decision]
- Reference B influenced: [high-level decision]
- Reference C influenced: [high-level decision]
- New expression / substantial difference: [how the design is genuinely original]
- No copied logos, illustrations, photos, or near-duplicate executions: [confirmed / not yet checked]
```

Do not write fabricated `x of n` observations: count actual verified examples, or describe patterns qualitatively.

## 4. Pattern extraction decision process

- Compare references side by side or by structured notes: which broad solutions repeat? Which are rare but particularly effective?
- Look for underlying mechanics, not just appearance. For example: a 65%-empty canvas can work because the focal product has strong material contrast, *not* because all premium campaigns require 65% empty space.
- Separately evaluate **effectiveness for this brief** versus **frequency**. A recurring style can be wrong for a client's audience.
- Choose one clear design grammar; reject contradictory combinations rather than using every interesting technique.

## 5. Adaptation and ethics

Use references as **influence**, not assets or blueprints to duplicate:
- **One-reference reinterpretation:** Borrow a general principle (e.g. diagonal subject placement with large quiet zone) but invent new subject staging, crop, scale, copy treatment, color system, and art direction. Do not recreate a recognizable signature composition pixel-for-pixel.
- **Two–three-reference synthesis:** Borrow broad layout strategy from A, palette relationship from B, typographic hierarchy from C. Add a new concept and brand-specific visual decision, not just a collage.
- **Never:** copy a creator's bespoke illustration, photograph, trademark, logo, proprietary visual system, or a recognizable design wholesale; swap only the brand/title and call it new.

Document influence URLs in `Design Direction` and retain the internal scratchpad. Present credited reference links if the user asks for research or when showing a moodboard.

## 6. Quality gate before production

Answer internally:
1. Are the references authentic, relevant, varied, and attributable?
2. Is the intended audience aesthetic visible in the selected pattern language?
3. Does the concept maintain strong negative space, typography, and one hero idea?
4. Is the proposed design demonstrably distinct from each source reference?
5. Are product assets, logos, and exact facts preserved?
6. If the research sample was small or inaccessible, have we avoided overstating confidence?

If the answer to #4 is no, redesign before generating imagery.

## Production constraints

Learn general principles, but never import decorative text rules/strokes or a filled footer from references. Reserve the bottom 12% by default. Execute the entire advertisement through ChatGPT Image, including requested typography.
