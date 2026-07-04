# Trivpass Content Library

Social content is stored **one folder per post**:

```
content/{year}/{month}/{date}-{title}/
```

- `{year}` — 4-digit, e.g. `2026`
- `{month}` — 2-digit numeric, e.g. `06`
- `{date}` — 2-digit day of month, e.g. `22`
- `{title}` — kebab-case slug, e.g. `driver-vetting`

Example: `content/2026/06/22-driver-vetting/`

## Each post folder contains

| File | Purpose |
|---|---|
| `brief.md` | Pillar, format, date, slide-by-slide copy, caption, hashtags, status |
| `prompts.md` | AI image-generation prompts — one per slide, following the locked layout |
| `assets/` | Generated / final images (1080×1350, 4:5) |

## Conventions

- Brand voice, CTA discipline, and the image-prompt + slide-layout rules live in
  [`skills/trivpass-content-planner/references/content-output.md`](../skills/trivpass-content-planner/references/content-output.md).
- Slide layout is locked: **logo at the top, above the title** → eyebrow → title → body → photo.
- Status values: `Draft`, `Needs asset`, `Ready`, `Scheduled`, `Posted`.
