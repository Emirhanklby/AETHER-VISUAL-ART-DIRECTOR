# Platform safe zones — Instagram Feed

These are the **user-specified design guidelines** for preparing Instagram Feed visuals and anticipating a centered **3:4** crop in the profile grid. UI implementations can change; test with the actual target placement when possible.

## Feed post, square (1080 × 1080 px)

- **Minimum edge inset:** 60 px per side.
- **Full-feed content-safe rectangle:** `x: 60–1020`, `y: 60–1020`.
- **Centered 3:4 profile-grid crop:** when the preview displays the full 1080 px height, the 3:4 width is `(3/4) × 1080 = 810 px`. Side crop: `(1080−810)/2 = 135 px` per side.
- **Grid-visible rectangle:** `x: 135–945`, `y: 0–1080`.
- **Combined essential-content safe rectangle:** `x: 135–945`, `y: 60–1020`.

## Feed post, portrait (1080 × 1350 px)

- **Minimum edge inset:** 60 px per side.
- **Full-feed content-safe rectangle:** `x: 60–1020`, `y: 60–1290`.
- **Centered 3:4 profile-grid crop:** `(3/4) × 1350 = 1012.5 px` visible width. Side crop: `(1080−1012.5)/2 = 33.75 px` on each side (roughly 34 px).
- **Approximate grid-visible rectangle:** `x: 34–1046`, `y: 0–1350` (rounded).
- **Combined essential-content safe rectangle:** `x: 60–1020`, `y: 60–1290`; the 60 px perimeter is stricter than the approximately 34 px grid trim.

## What counts as critical content?

Campaign headline, product name, logo, offer or price, date, legal qualifiers when required, CTA if used, and distinctive product details that must be identifiable. Secondary background shapes or deliberate artistic crops may extend beyond safe areas.

## Practical production workflow

1. Confirm actual target dimensions (1080 × 1080 vs. 1080 × 1350).
2. Establish the combined safe content rectangle before placing text, logos, prices, and important subjects.
3. Make a considered composition with generous negative space inside and around the safe region; avoid automatically centering all elements.
4. Generate/render, then preview the full post and simulate the **centered 3:4 profile crop** at thumbnail scale.
5. If essential content clips or becomes illegible, reposition/re-scale critical elements and recheck.
6. If no image or render is available for inspection, include these rules in the prompt but do not report a completed crop verification.

> Scope: Instagram **Feed** only. Do not presume these measurements are correct for Stories, Reels, ads, or every version of the profile grid.