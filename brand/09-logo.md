# 09 · Logo Usage

> How to use the Trivpass logo — sizes, clear space, what not to do, and where each version lives.

---

## The three logo files

All three live in [logo/](logo/) in this folder. They are the production-ready SVGs.

| File | What it is | Use it on |
|---|---|---|
| `logo/trivpass-wordmark.svg` | **Wordmark** — `trivpass` in Fraunces serif, Jungle Green, with a Terracotta accent dot | Top-nav, footer brand block, email header, deck title slides, business cards, marketing-page hero corner |
| `logo/trivpass-mark.svg` | **Mark** — the ticket-pass icon in Jungle Green | Favicons, app icons, social-media avatars, watermarks, very small placements where the wordmark wouldn't be legible |
| `logo/trivpass-mark-reverse.svg` | **Reverse mark** — the ticket-pass icon for dark backgrounds | Footer dark-band brand block, business-card reverse, deck cover slides with a dark background, T-shirt prints on dark fabric |

### What each one looks like

- **Wordmark:** Lowercase `trivpass` in Fraunces 600 with a small Terracotta dot to the right. The dot is part of the wordmark and is never removed.
- **Mark:** The ticket-pass silhouette — a stylized ticket with a flowing flag tail. Inspired by Bali's *banten* (offering tray) and a paper boarding pass. Single-color silhouette in Jungle Green.
- **Reverse mark:** Same silhouette, for use on dark or jungle-green surfaces.

### The canonical lockup

The logo is most often shown as a **horizontal lockup of the mark + wordmark together** — the mark on the left, the wordmark on the right, vertically aligned to the wordmark's cap height. There isn't a separate combined-lockup SVG file; the lockup is composed inline (in HTML / Blade / Figma) using the mark and wordmark with appropriate spacing (approximately the height of the lowercase `t` between them).

---

## Construction & clear space

### Clear space

A safe **clear space equal to the height of the wordmark's cap** (or the mark's cap, for the mark version) must be kept around the logo on all sides.

```
                       ← clear-space →
                       │             │
   ──────              ┌─────────────┐               ──────
     ↑                 │             │                 ↑
   clear-              │   LOGO      │              clear-
   space               │             │              space
     ↓                 └─────────────┘                 ↓
   ──────                                            ──────
                       │             │
                       ← clear-space →
```

No other element (button, photograph, headline, page edge) may enter that clear-space zone.

### Minimum size

- **Wordmark:** Never displayed below **96px wide** on screen, or **24mm wide** in print. Below that, switch to the mark.
- **Mark:** Never displayed below **24×24px** on screen, or **8mm** in print. Below that, drop the logo from the surface entirely — there is no version of the mark that reads at < 24px.
- **Circular verified mark** (the inline trust mark, not the brand logo) has a 16×16px minimum.

---

## Colorways

The logo ships in **two colorways** — that's the entire range. No other color combinations are acceptable.

| Colorway | When to use | Wordmark | Mark | Background |
|---|---|---|---|---|
| **Jungle Green on off-white** (default) | 95% of surfaces | `#1f4d3a` Jungle Green | `#1f4d3a` Jungle Green | Off-white `#faf7f2` (or surface 1–3) |
| **Reverse — off-white on Jungle Green** | Footer dark-band, business-card backs, T-shirt prints on dark fabric, deck cover slides with a dark background | `#faf7f2` Off-white | `#faf7f2` Off-white | Jungle Green `#1f4d3a` |

The Terracotta dot on the wordmark is always **`#c2603e` Terracotta** — even on the reverse colorway. The dot does not invert.

---

## Placement

### Top-nav

- The lockup (mark + wordmark), flush left.
- Wordmark cap ~28px tall.
- Vertically centered in the 72px nav band.
- 24px left padding from the page-grid edge.

### Footer

- The lockup, in the upper-left block of the footer.
- Wordmark cap ~28px tall.
- Followed by the tagline *"The real Bali, uncomplicated."* in Inter 14px muted.

### Email header

- The lockup, centered, wordmark cap ~28px tall.
- 32px top padding from the email-header background.
- Background: off-white.

### Favicon / app icon

- The **mark**, not the wordmark.
- 32×32px and 16×16px PNGs derived from the SVG.
- A Jungle Green filled-square background may be used for OS icon containers that require it (iOS, Android, macOS dock).

### Deck title slide

- Either the lockup (centered, wordmark cap ~120px) or the reverse mark (on a Jungle Green full-bleed background).
- Never the mark alone on a deck title slide — the wordmark is the more legible choice.

### Business card

- Front: lockup, top-left, wordmark cap ~24px. Card on off-white.
- Back: reverse mark, centered, on Jungle Green full-bleed.

### Social media avatar

- The mark, on an off-white-filled square or circle.
- The reverse mark on Jungle Green is acceptable for platforms where Trivpass typically posts on dark backgrounds.

---

## Don't

A short list of things never to do with the Trivpass logo:

- ❌ **Don't change the colors.** Jungle Green (`#1f4d3a`) and Terracotta (`#c2603e`) are the only acceptable values. No teal, no navy, no near-black.
- ❌ **Don't remove the Terracotta dot** from the wordmark. It's part of the wordmark, not decoration.
- ❌ **Don't change the dot color.** Even on the reverse colorway, the dot stays Terracotta.
- ❌ **Don't replace Fraunces** with a generic serif or sans for the wordmark. If Fraunces is unavailable, the SVG already carries it as embedded text — use the SVG, not a re-typed version.
- ❌ **Don't stretch, skew, or rotate** the wordmark or the mark.
- ❌ **Don't add a drop shadow, outer glow, or stroke** to the logo.
- ❌ **Don't place the logo on a photograph** without an off-white lockup block behind it. The logo must sit on a solid surface, not on the photograph itself.
- ❌ **Don't recolor the logo** to match a hotel partner's brand or a press-publication's house style. We keep our colors.
- ❌ **Don't display the wordmark below 96px wide**, or the mark below 24×24px. Drop the logo from the surface entirely if there isn't room.
- ❌ **Don't tagline-lock** the logo. The tagline *"The real Bali, uncomplicated."* is a separate type element; it never integrates into the logo itself.
- ❌ **Don't substitute the v3 Smoke-Ink palette** (`#2a2520`) or any previous-iteration variant. The current production logo is Jungle Green on warm off-white.

---

## File format guidance

- **SVG** is the production format for all web and print. The files in [logo/](logo/) are SVG.
- **PNG** is acceptable for legacy systems that can't render SVG. Export at 2x or 3x for retina. Always start from the SVG; never compress through JPEG.
- **PDF** for print press files. Export from the SVG; never rasterize.
- **EPS** is not maintained. If a press partner asks for EPS, export from the SVG with Inkscape or Illustrator.

---

## Where to find each version

| Use case | File path |
|---|---|
| Brand book — wordmark | [logo/trivpass-wordmark.svg](logo/trivpass-wordmark.svg) |
| Brand book — mark | [logo/trivpass-mark.svg](logo/trivpass-mark.svg) |
| Brand book — reverse mark | [logo/trivpass-mark-reverse.svg](logo/trivpass-mark-reverse.svg) |
| In-product (Laravel app) mark | [`public/brand/mark.svg`](../../public/brand/mark.svg) |
| In-product (Laravel app) reverse | [`public/brand/mark-reverse.svg`](../../public/brand/mark-reverse.svg) |

The files in this brand book mirror the files in `public/brand/`. If the production logo changes, update both places.

---

## Note on the production reverse-mark file

The current production `public/brand/mark-reverse.svg` was generated during an earlier design iteration and still carries a Smoke Ink (`#2a2520`) background tone rather than a Jungle Green field. The mark silhouette itself reads correctly on dark surfaces, but for strict brand-colorway alignment, a clean Jungle Green `#1f4d3a` background should be regenerated when convenient. (Flagging here for the design team; it does not affect day-to-day use.)
