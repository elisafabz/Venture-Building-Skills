---
name: meta-social-images
description: Use when the user wants to create Meta (Facebook/Instagram) profile pictures and cover images for a brand or venture. Triggered by requests like "profile picture for Meta", "cover image for Facebook", "create social media images", "Meta branding".
model: sonnet
effort: low
---

# Meta Social Media Images

Generate pixel-perfect Meta profile pictures and cover images using the project's real brand assets (fonts, colors, logo).

## Why Pillow, Not AI Generation

AI image generators (Gemini, DALL-E) can't reproduce exact fonts, logo marks, or brand colors reliably. This skill uses **Python Pillow** with the project's actual font files to guarantee brand consistency.

## Step 0: Gather Brand Info

Before generating anything, collect these from the project:

```
Scanning project for brand assets...

- [ ] Brand name and logo mark
- [ ] Font files (.ttf) — headline + body fonts
- [ ] Color palette — bg, fg, accent, muted, secondary colors
- [ ] Tagline / claim
- [ ] Key messaging (pillars, value props, subtitle)
- [ ] Launch date or CTA (if applicable)
```

**Where to look:**
1. Project CLAUDE.md (design system section)
2. Any existing brand or project notes
3. `src/index.css` or design tokens file
4. `public/` folder for logos, favicons
5. Font files in project (search `**/*.ttf`)

## Step 1: Locate Font Files

Search the project for `.ttf` files:
```
**/*.ttf
```

You need at minimum:
- **Headline font** (bold weight) — for logo and brand name
- **Body font** (regular weight) — for subtitles, taglines

**If no `.ttf` is found in the project: STOP and ask the user for the font file or font name.** Never silently substitute a system font for the headline/logo font — a wrong logo font defeats the entire purpose of this skill. System-font fallback is acceptable only for the *body* font, and only after telling the user.

Watch out: some projects load fonts via Google Fonts CDN (check `index.html` / `index.css` for `fonts.googleapis.com`). In that case, download the exact `.ttf` from Google Fonts first (or ask the user for it) — do not approximate.

## Step 2: Generate Images

Create a Python script that generates **4 profile + 4 cover variants**.

### Dimensions

| Asset | Size | Notes |
|-------|------|-------|
| Profile picture | 1080x1080 | Displayed as circle on Meta |
| Cover image (Facebook) | 1640x624 | 2x retina of 820x312 |

### The 4 Variants

| # | Name | Profile | Cover |
|---|------|---------|-------|
| 1 | **Minimal Hell** | Logo mark on light bg | Wordmark + tagline on light bg |
| 2 | **Dark Mode** | Logo mark inverted on dark bg | Wordmark + pillars/messaging on dark bg |
| 3 | **Accent Shape** | Logo mark on colored shape (circle/square) | Accent color bands + wordmark + subtitle |
| 4 | **Brand Color** | Logo mark inverted on accent bg | Split design: accent bg left + wordmark right |

### Script Template

Adapt this template to the project's brand. Replace all `{BRAND_*}` placeholders:

```python
#!/usr/bin/env python3
"""Generate Meta social media images for {BRAND_NAME}."""

from PIL import Image, ImageDraw, ImageFont
import os

OUT = "{OUTPUT_DIR}"
os.makedirs(OUT, exist_ok=True)

# ── Brand Colors (from project design system) ──
BG      = {BRAND_BG}       # e.g. (244, 241, 236)
FG      = {BRAND_FG}       # e.g. (13, 12, 10)
ACCENT  = {BRAND_ACCENT}   # e.g. (192, 92, 69)
MUTED   = {BRAND_MUTED}    # e.g. (79, 74, 66)
SECONDARY = {BRAND_SECONDARY}  # e.g. (202, 213, 195)
DARK    = {BRAND_DARK}     # e.g. (20, 18, 16)

# ── Fonts ──
FONT_HEADLINE = "{PATH_TO_HEADLINE_FONT_TTF}"
FONT_BODY = "{PATH_TO_BODY_FONT_TTF}"  # fallback to system font if not available

font_bold = lambda s: ImageFont.truetype(FONT_HEADLINE, s)

def font_body(s):
    if os.path.exists(FONT_BODY):
        return ImageFont.truetype(FONT_BODY, s)
    for p in ["/System/Library/Fonts/Supplemental/Arial.ttf",
              "/System/Library/Fonts/Helvetica.ttc"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, s)
    return ImageFont.load_default()

# ── Brand Elements ──
BRAND_NAME = "{BRAND_NAME}"           # e.g. "yourbrand"
BRAND_MARK = "{BRAND_MARK}"           # e.g. "a" (short logo mark for profile)
TAGLINE = "{BRAND_TAGLINE}"           # e.g. "Conversations become action."
SUBTITLE = "{BRAND_SUBTITLE}"         # e.g. "The relationship app for couples..."
PILLARS = "{BRAND_PILLARS}"           # e.g. "Connect · Plan · Clarify · Understand"
LAUNCH_INFO = "{BRAND_LAUNCH_INFO}"   # e.g. "Coming Soon · Mai 2026" or ""

# Set HAS_DOT_MARK = True if brand uses a special dot/symbol after text
HAS_DOT_MARK = {HAS_DOT_MARK}  # True/False
DOT_COLOR = {DOT_COLOR}        # color for the dot, e.g. ACCENT


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HELPERS — adapt draw_logo_mark and draw_wordmark
# to match the brand's exact logo construction
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def draw_logo_mark(draw, cx, cy, size, fg_color=FG, dot_color=DOT_COLOR):
    """Draw the short logo mark centered at (cx, cy)."""
    f = font_bold(size)
    bbox = f.getbbox(BRAND_MARK)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    if HAS_DOT_MARK:
        dot_r = int(size * 0.09)
        dot_gap = int(size * 0.06)
        total_w = w + dot_gap + dot_r * 2
        x = cx - total_w // 2
        y = cy - h // 2 - bbox[1]
        draw.text((x, y), BRAND_MARK, font=f, fill=fg_color)
        dot_cx = x + w + dot_gap + dot_r
        dot_cy = y + bbox[3] - dot_r
        draw.ellipse([dot_cx - dot_r, dot_cy - dot_r,
                       dot_cx + dot_r, dot_cy + dot_r], fill=dot_color)
    else:
        x = cx - w // 2
        y = cy - h // 2 - bbox[1]
        draw.text((x, y), BRAND_MARK, font=f, fill=fg_color)


def draw_wordmark(draw, cx, cy, size, fg_color=FG, dot_color=DOT_COLOR):
    """Draw the full brand name centered at (cx, cy). Returns baseline y."""
    f = font_bold(size)
    bbox = f.getbbox(BRAND_NAME)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]

    if HAS_DOT_MARK:
        dot_r = int(size * 0.085)
        dot_gap = int(size * 0.08)
        total_w = w + dot_gap + dot_r * 2
        x = cx - total_w // 2
        y = cy - h // 2 - bbox[1]
        draw.text((x, y), BRAND_NAME, font=f, fill=fg_color)
        dot_cx = x + w + dot_gap + dot_r
        dot_cy = y + bbox[3] - dot_r
        draw.ellipse([dot_cx - dot_r, dot_cy - dot_r,
                       dot_cx + dot_r, dot_cy + dot_r], fill=dot_color)
    else:
        x = cx - w // 2
        y = cy - h // 2 - bbox[1]
        draw.text((x, y), BRAND_NAME, font=f, fill=fg_color)

    return y + bbox[3]


def draw_centered_text(draw, cx, y, text, size, color=MUTED):
    """Draw centered text at given position."""
    f = font_body(size)
    bbox = f.getbbox(text)
    w = bbox[2] - bbox[0]
    draw.text((cx - w // 2, y), text, font=f, fill=color)


def draw_thin_line(draw, cx, y, width, color=ACCENT):
    """Draw a thin horizontal accent line."""
    draw.line([(cx - width // 2, y), (cx + width // 2, y)], fill=color, width=2)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROFILE PICTURES (1080x1080)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

S = 1080

# V1: Light background
img = Image.new("RGB", (S, S), BG)
draw_logo_mark(ImageDraw.Draw(img), S//2, S//2, 420, FG, DOT_COLOR)
img.save(f"{OUT}/profile-v1-minimal.png", quality=95)

# V2: Dark background
img = Image.new("RGB", (S, S), DARK)
draw_logo_mark(ImageDraw.Draw(img), S//2, S//2, 420, BG, ACCENT)
img.save(f"{OUT}/profile-v2-dark.png", quality=95)

# V3: Accent shape (colored circle on light bg)
img = Image.new("RGB", (S, S), BG)
d = ImageDraw.Draw(img)
r = 380
d.ellipse([S//2-r, S//2-r, S//2+r, S//2+r], fill=SECONDARY)
draw_logo_mark(d, S//2, S//2, 400, FG, DOT_COLOR)
img.save(f"{OUT}/profile-v3-accent.png", quality=95)

# V4: Accent background
img = Image.new("RGB", (S, S), ACCENT)
draw_logo_mark(ImageDraw.Draw(img), S//2, S//2, 420, BG, (255, 245, 235))
img.save(f"{OUT}/profile-v4-brand.png", quality=95)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COVER IMAGES (1640x624)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

W, H = 1640, 624

# V1: Light + wordmark + tagline
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
bl = draw_wordmark(d, W//2, H//2-40, 120, FG, DOT_COLOR)
draw_thin_line(d, W//2, bl+24, 80, ACCENT)
draw_centered_text(d, W//2, bl+44, TAGLINE, 32, MUTED)
img.save(f"{OUT}/cover-v1-minimal.png", quality=95)

# V2: Dark + wordmark + pillars
img = Image.new("RGB", (W, H), DARK)
d = ImageDraw.Draw(img)
bl = draw_wordmark(d, W//2, H//2-30, 110, BG, ACCENT)
draw_thin_line(d, W//2, bl+20, 80, ACCENT)
draw_centered_text(d, W//2, bl+36, PILLARS, 26, (160, 155, 148))
img.save(f"{OUT}/cover-v2-dark.png", quality=95)

# V3: Accent bands + wordmark + subtitle
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
d.rectangle([0, 0, W, 8], fill=SECONDARY)
d.rectangle([0, H-8, W, H], fill=SECONDARY)
bl = draw_wordmark(d, W//2, H//2-30, 110, FG, DOT_COLOR)
draw_centered_text(d, W//2, bl+30, SUBTITLE, 28, MUTED)
img.save(f"{OUT}/cover-v3-accent.png", quality=95)

# V4: Split — accent left, light right + launch info
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
split = W // 3
d.rectangle([0, 0, split, H], fill=ACCENT)
draw_logo_mark(d, split//2, H//2, 240, BG, (255, 245, 235))
rcx = split + (W - split) // 2
bl = draw_wordmark(d, rcx, H//2-30, 100, FG, DOT_COLOR)
if LAUNCH_INFO:
    draw_centered_text(d, rcx, bl+24, LAUNCH_INFO, 26, MUTED)
img.save(f"{OUT}/cover-v4-split.png", quality=95)

print(f"\n✅ 8 images generated in {OUT}")
```

## Step 3: Run and Review

1. Execute the script
2. Show all 8 images to the user using the Read tool
3. Present them organized: profiles first, then covers

## Step 4: Iterate

Ask the user which variants they like and what to adjust. Common tweaks:
- Font size / spacing
- Dot/mark size or position
- Background color swaps
- Different text content on covers
- Adding/removing elements

## Adapting for Different Logo Types

| Logo Type | `BRAND_MARK` | `HAS_DOT_MARK` | Notes |
|-----------|-------------|-----------------|-------|
| Text + dot/symbol | First letter | `True` | Like "brandname●" → mark is "b" |
| Pure wordmark | First letter(s) | `False` | Like "notion" → mark is "N" |
| Icon + text | N/A | N/A | Compose icon PNG onto canvas with `Image.paste()` |
| Initials | Initials | `False` | Like "ABC" → mark is "ABC" |

For icon-based logos, load the icon PNG and paste it centered instead of drawing text.

## Edge Cases

- **Colors defined as hex or oklch in CSS:** Pillow needs RGB tuples. Convert hex → `(r, g, b)` yourself. For `oklch(...)` values, convert via a quick Python snippet or ask the user for the hex equivalent — never eyeball-approximate brand colors.
- **Missing brand colors:** If the project defines fewer colors than the template needs (e.g. no SECONDARY or DARK), derive them conservatively (DARK = near-black tinted toward BG hue; SECONDARY = muted ACCENT) and tell the user which colors were derived. Never invent a new hue.
- **Text overflow:** Before saving, check the rendered text width against the canvas (`font.getbbox`). If TAGLINE/PILLARS/SUBTITLE is wider than ~85% of the canvas, reduce font size stepwise until it fits — do not let text touch the edges or get cropped.
- **Accents and special characters:** verify the chosen `.ttf` actually renders every character your tagline needs (accents, umlauts, cedillas). If glyphs render as boxes, the font file is missing them — ask for an alternative weight or file.
- **Instagram:** Instagram has NO cover image — only the 1080x1080 profile picture applies. Don't promise IG covers; the cover variants are Facebook-only.
- **Icon-based logos (no wordmark font):** Skip `draw_logo_mark` text rendering entirely; load the logo PNG/SVG-export and `Image.paste()` it centered (use the alpha channel as mask).

## Rules

- **Always use real font files** — never rely on AI to approximate typography
- **Always read brand guidelines first** — colors must be exact values from the design system, converted to RGB tuples
- **Output directory**: `<marketing assets folder>/meta-images/` — marketing assets NEVER go into the git repo (global rule: Code → Repo, Content → Desktop). If the venture's Desktop folder is unclear, ask.
- **Profile images are circles on Meta** — keep content centered inside an inner circle of ~70% radius; corners get cropped
- **Facebook cover safe zone**: important content in center 60%, profile pic overlaps bottom-left on desktop and mobile crops the sides — nothing critical in the outer ~200px
- PNG format, quality=95
