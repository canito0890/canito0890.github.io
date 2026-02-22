# Revised Frontend Design Plan: Tokyo Night Design System Overhaul

## Summary

Complete design system overhaul for the Jekyll blog: replace Inter with Geist font, rebrand from "Synthwave" to "Tokyo Night", fix hardcoded legacy colors, distribute accent colors across UI, add fluid typography, scroll-triggered animations, background texture/depth, grid-breaking design elements, generate missing assets, and remove legacy files.

All changes follow the [frontend design skill](../../.github/skills/front-design/SKILL.md) guidelines.

---

## Step 1: Replace Inter with Geist Font

**Files:** `_includes/head/custom.html`, `assets/css/main.scss`

### In `_includes/head/custom.html`

Replace the Inter Google Font import with Geist from Vercel's CDN:

```html
<!-- REMOVE -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Righteous&display=swap" rel="stylesheet">

<!-- REPLACE WITH -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link href="https://cdn.jsdelivr.net/npm/geist@latest/dist/fonts/geist-sans/style.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Righteous&display=swap" rel="stylesheet">
```

### In `assets/css/main.scss`

Change the `--font-body` custom property:

```css
/* BEFORE */
--font-body: 'Inter', sans-serif;

/* AFTER */
--font-body: 'Geist', sans-serif;
```

No other changes needed — all body text references use `var(--font-body)`.

---

## Step 2: Fix ALL Hardcoded Old Synthwave Colors

**Files:** `assets/css/main.scss`, `index.markdown`, `_posts/2026-02-05-synthwave-redesign-deep-dive.markdown`

The old synthwave background `#0f0f1e` = `rgb(15, 15, 30)` appears as `rgba(15, 15, 30, ...)` in multiple places. The old synthwave cyan `#00d9ff` = `rgb(0, 217, 255)` also appears. All must be updated to Tokyo Night equivalents.

### In `assets/css/main.scss`

| Location | Current | Replacement |
|----------|---------|-------------|
| `.masthead` background | `rgba(15, 15, 30, 0.95)` | `rgba(26, 27, 38, 0.95)` |
| `.page__hero--overlay` gradient | `rgba(15, 15, 30, 0.7)` + `rgba(26, 26, 62, 0.9)` | `rgba(26, 27, 38, 0.7)` + `rgba(36, 40, 59, 0.9)` |
| `.page__footer` background | `rgba(15, 15, 30, 0.95)` | `rgba(26, 27, 38, 0.95)` |
| `tr:hover td` background | `rgba(0, 217, 255, 0.05)` | `rgba(125, 207, 255, 0.05)` |
| `.pagination--pager:hover` background | `rgba(0, 217, 255, 0.1)` | `rgba(125, 207, 255, 0.1)` |

### In `index.markdown`

```yaml
# BEFORE
overlay_color: "#0f0f1e"

# AFTER
overlay_color: "#1A1B26"
```

### In `_posts/2026-02-05-synthwave-redesign-deep-dive.markdown`

```yaml
# BEFORE
overlay_color: "#0f0f1e"

# AFTER
overlay_color: "#1A1B26"
```

---

## Step 3: Rename Design System in CSS Comments

**File:** `assets/css/main.scss`

```css
/* BEFORE */
/* ============================================
   SYNTHWAVE DESIGN SYSTEM
   Outrun/Retro-Futuristic Theme
   ============================================ */

/* CSS Custom Properties (Design Tokens) - Tokyo Night Theme */

/* AFTER */
/* ============================================
   TOKYO NIGHT DESIGN SYSTEM
   Developer-Centric Dark Theme
   ============================================ */

/* CSS Custom Properties (Design Tokens) */
```

Also update the syntax highlighting comment:

```css
/* BEFORE */
/* Tokyo Night syntax highlighting */

/* AFTER (no change needed — this one is already correct) */
```

---

## Step 4: Fix `.notice--success` to Use Design Token

**File:** `assets/css/main.scss`

```css
/* BEFORE */
.notice--success {
  border-left-color: #00ff88;
}

/* AFTER */
.notice--success {
  border-left-color: var(--accent-green);
}
```

---

## Step 5: Fix `.notice--warning` Semantic Color

**File:** `assets/css/main.scss`

```css
/* BEFORE */
.notice--warning {
  border-left-color: var(--accent-blue);
}

/* AFTER */
.notice--warning {
  border-left-color: var(--accent-orange);
}
```

---

## Step 6: Distribute Accent Colors Across UI

**File:** `assets/css/main.scss`

Semantic color mapping:

| Color | Token | UI Usage |
|-------|-------|----------|
| Blue `#7AA2F7` | `--accent-blue` | Primary links, active states, `.notice` (default), `h1` color — **keep as-is** |
| Purple `#BB9AF7` | `--accent-purple` | Hover glows, card accents, `h2` color, blockquote border — **keep as-is** |
| Cyan `#7DCFFF` | `--accent-cyan` | Inline code, link text, `.notice` default — **keep as-is** |
| Green `#9ECE6A` | `--accent-green` | **NEW:** `.notice--success` border (step 4), `.notice--info` if needed |
| Orange `#FF9E64` | `--accent-orange` | **NEW:** `.notice--warning` border (step 5), date/time metadata |
| Yellow `#E0AF68` | `--accent-yellow` | **NEW:** Blockquote cite/attribution, `<mark>` highlight styling |
| Red `#F7768E` | `--accent-red` | **NEW:** `.notice--danger` border |

### New styles to add:

```css
/* Notice - Danger */
.notice--danger {
  border-left-color: var(--accent-red);
}

/* Date metadata styling */
.page__meta,
.archive__item .page__meta {
  color: var(--accent-orange);
  font-family: var(--font-mono);
  font-size: 0.8em;
  letter-spacing: 0.02em;
}

/* Mark/highlight styling */
mark {
  background: rgba(224, 175, 104, 0.15);
  color: var(--accent-yellow);
  padding: 0.1em 0.3em;
  border-radius: 3px;
}

/* Blockquote citation */
blockquote cite,
blockquote footer {
  color: var(--accent-yellow);
  font-style: normal;
  font-size: 0.9em;
}
```

---

## Step 7: Fluid Typography with `clamp()`

**File:** `assets/css/main.scss`

### Add fluid type sizes

```css
/* In the :root custom properties block, add: */
--type-hero: clamp(2rem, 5vw, 3.5rem);
--type-h1: clamp(1.75rem, 3.5vw, 2.75rem);
--type-h2: clamp(1.4rem, 2.5vw, 2rem);
--type-h3: clamp(1.15rem, 2vw, 1.5rem);
--type-h4: clamp(1rem, 1.5vw, 1.25rem);
--type-body: clamp(0.95rem, 1.1vw, 1.1rem);
--type-small: clamp(0.8rem, 0.9vw, 0.9rem);
```

### Apply to elements

```css
body { font-size: var(--type-body); }

h1 { font-size: var(--type-h1); letter-spacing: -0.02em; }
h2 { font-size: var(--type-h2); letter-spacing: -0.01em; }
h3 { font-size: var(--type-h3); }
h4 { font-size: var(--type-h4); }

.page__title { font-size: var(--type-hero); }
.page__lead { font-size: clamp(1rem, 1.5vw, 1.3rem); }
.hero-tagline { font-size: clamp(0.95rem, 1.3vw, 1.2rem); }
```

### CRITICAL: Remove conflicting media query font-size rules

These fixed font-size rules in breakpoints will override `clamp()` and must be **deleted**:

```css
/* DELETE from @media (max-width: 1024px): */
.page__title { font-size: 3em; }

/* DELETE from @media (max-width: 768px): */
.page__title { font-size: 2.2em; }
.page__lead { font-size: 1.1em; }
.hero-tagline { font-size: 1.1em; }
.archive__item-title { font-size: 1.3em; }
.page__content h2 { font-size: 1.6em; }

/* DELETE from @media (max-width: 480px): */
.page__title { font-size: 1.8em; }
.hero-tagline { font-size: 1em; }
.btn { font-size: 0.9em; }
```

Keep all other rules in those breakpoints (padding, display, grid-size, etc.).

---

## Step 8: Scroll-Triggered Animations & Hero Enhancement

**File:** `assets/css/main.scss`

### Visibility-safe defaults (CRITICAL)

The current `animation: fadeInUp 0.5s ease-out backwards` on `.page__content > *` uses `backwards` fill mode, meaning elements start invisible. This is risky — if animation fails to trigger, content is invisible forever.

**Fix**: Change to forward-only animation that starts visible:

```css
/* BEFORE */
.page__content > * {
  animation: fadeInUp 0.5s ease-out backwards;
}

/* AFTER */
.page__content > * {
  animation: fadeInUp 0.5s ease-out both;
}
```

### Hero entrance enhancement

Add a gradient sweep animation on the page title:

```css
.page__title {
  background: linear-gradient(
    90deg,
    var(--accent-blue) 0%,
    var(--accent-purple) 40%,
    var(--accent-cyan) 60%,
    var(--text-primary) 100%
  );
  background-size: 200% 100%;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientSweep 1.5s ease-out forwards, fadeInUp 0.6s ease-out;
}

@keyframes gradientSweep {
  from { background-position: 100% 50%; }
  to { background-position: 0% 50%; }
}
```

### Scroll-triggered reveals for archive items

Use `animation-timeline: view()` with `@supports` guard so non-supporting browsers see content normally:

```css
/* Scroll-triggered animations — progressive enhancement only */
@supports (animation-timeline: view()) {
  .archive__item {
    opacity: 0;
    transform: translateY(30px);
    animation: fadeInUp 0.6s ease-out both;
    animation-timeline: view();
    animation-range: entry 0% entry 30%;
  }

  .archive__item:nth-child(even) {
    animation-delay: 0.1s;
  }
}
```

**Key**: Without `@supports`, archive items remain `opacity: 1` (default) — no invisible content risk.

---

## Step 9: Background Texture & Depth

**File:** `assets/css/main.scss`

### Increase grid visibility from 3% to 5%

```css
/* BEFORE */
background-image:
  linear-gradient(rgba(122, 162, 247, 0.03) 1px, transparent 1px),
  linear-gradient(90deg, rgba(122, 162, 247, 0.03) 1px, transparent 1px);

/* AFTER */
background-image:
  linear-gradient(rgba(122, 162, 247, 0.05) 1px, transparent 1px),
  linear-gradient(90deg, rgba(122, 162, 247, 0.05) 1px, transparent 1px);
```

### Add noise grain overlay via `body::after`

```css
body::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.025;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
  mix-blend-mode: overlay;
}
```

### Add secondary radial glow (asymmetric)

Update the body background to include a purple radial glow anchored bottom-right:

```css
/* BEFORE */
body {
  background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  background-attachment: fixed;
}

/* AFTER */
body {
  background:
    radial-gradient(ellipse at 85% 85%, rgba(187, 154, 247, 0.04) 0%, transparent 50%),
    linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
  background-attachment: fixed;
}
```

---

## Step 10: Grid-Breaking Design Elements

**File:** `assets/css/main.scss`

### Floating gradient orb behind hero

```css
.page__hero--overlay::after {
  content: '';
  position: absolute;
  top: -20%;
  right: -10%;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(122, 162, 247, 0.08) 0%,
    rgba(187, 154, 247, 0.04) 40%,
    transparent 70%
  );
  filter: blur(60px);
  pointer-events: none;
  z-index: 0;
}
```

### Oversized decorative blockquote marks

```css
blockquote {
  position: relative;
  overflow: visible;
}

blockquote::before {
  content: '"';
  position: absolute;
  top: -0.3em;
  left: -0.15em;
  font-family: var(--font-display);
  font-size: 4em;
  color: var(--accent-purple);
  opacity: 0.12;
  line-height: 1;
  pointer-events: none;
}
```

### Diagonal divider between hero and content

```css
.page__hero--overlay {
  clip-path: polygon(0 0, 100% 0, 100% calc(100% - 30px), 0 100%);
  padding-bottom: calc(2em + 30px); /* compensate for clip */
}
```

---

## Step 11: Update Print Styles

**File:** `assets/css/main.scss`

Add to the existing `@media print` block:

```css
@media print {
  /* Existing rules... */

  /* Hide decorative elements */
  body::before,
  body::after,
  .page__hero--overlay::before,
  .page__hero--overlay::after {
    display: none;
  }

  /* Disable animations */
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
  }
}
```

---

## Step 12: Clean Up Duplicate `.archive__item:hover`

**File:** `assets/css/main.scss`

The `.archive__item:hover` rule is defined twice (once standalone at ~line 300, once grouped with `.toc:hover` at ~line 313). Consolidate into a single rule:

```css
/* BEFORE (two separate blocks) */
.archive__item:hover {
  transform: translateY(-6px);
  box-shadow: var(--glow-purple);
  border-color: rgba(187, 154, 247, 0.4);
}

/* ... later ... */

.archive__item:hover,
.toc:hover {
  transform: translateY(-6px);
  box-shadow: var(--glow-purple);
  border-color: rgba(187, 154, 247, 0.4);
}

/* AFTER (single grouped rule, remove the standalone) */
.archive__item:hover,
.toc:hover {
  transform: translateY(-6px);
  box-shadow: var(--glow-purple);
  border-color: rgba(187, 154, 247, 0.4);
}
```

---

## Step 13: Suppress `::before` Arrow on Nav Links

**File:** `assets/css/main.scss`

Add to the greedy-nav section:

```css
.greedy-nav a::before {
  display: none;
}
```

This prevents the external link arrow `↗` from appearing on the GitHub navigation link.

---

## Step 14: Create Favicon

**Files:** `assets/images/favicon.svg` (new), `_includes/head/custom.html`

### Create SVG favicon

Create a simplified version of `bio-photo.svg` that works at 16x16px — just the "JC" initials on a gradient background circle.

### Add to `_includes/head/custom.html`

```html
<link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/images/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/images/apple-touch-icon.png">
```

**Note:** PNG versions (`favicon-32x32.png`, `apple-touch-icon.png`) require external conversion from the SVG using ImageMagick, Inkscape, or an online tool like realfavicongenerator.net. The SVG favicon alone provides good coverage for modern browsers.

---

## Step 15: Create OG Image

**File:** `assets/images/og-image.png` (new)

Create a 1200×630 PNG with:
- Tokyo Night gradient background (`#1A1B26` → `#24283B`)
- Site title "Joel Cano" in Righteous font
- Subtitle "Software Developer & Technology Enthusiast"
- Decorative blue/purple gradient accent elements
- Match the SVG avatar aesthetic

**Note:** This requires an external image tool (Figma, GIMP, ImageMagick). Cannot be generated as pure code in the Jekyll project. The `_config.yml` already references this path (`og_image: /assets/images/og-image.png`).

---

## Step 16: Handle Blog Post Identity

**File:** `_posts/2026-02-05-synthwave-redesign-deep-dive.markdown`

Rather than rewriting 236 lines of narrative content, add a disclaimer note at the top of the post (after front matter):

```markdown
> **Note (February 2026):** This post was written during the initial design concept phase when the site used an Outrun/Synthwave palette. The design has since evolved into a **Tokyo Night** aesthetic with updated colors, Geist typography, and enhanced visual effects. The design process and architectural decisions described here remain accurate — only the specific color values have changed.
{: .notice--info}
```

Also update the front matter:
- Change `overlay_color` to `"#1A1B26"` (step 2)
- Update tags to include `tokyo-night` alongside `synthwave` for historical reference

---

## Step 17: Remove Legacy `blog/` Directory

**Files to delete:** `blog/atom.xml`, `blog/index.html`, `blog/` directory

These are artifacts from before the Minimal Mistakes theme migration:
- `blog/index.html` — basic post listing, replaced by the home layout + year-archive
- `blog/atom.xml` — old Atom feed, replaced by `jekyll-feed` plugin

Confirm they're not referenced anywhere:
- Not in `_config.yml` ✓
- Not in `_data/navigation.yml` ✓
- Not in any `_pages/` files ✓
- Uses old URL format (`http://` not `https://`) confirming staleness ✓

```bash
rm -rf blog/
```

---

## Verification Checklist

After all changes:

- [ ] `bundle exec jekyll clean && bundle exec jekyll serve` — no build errors
- [ ] Hero overlay color matches body background seamlessly (no visible seam)
- [ ] Geist font renders correctly — check Network tab for successful CDN load
- [ ] No FOUT/FOIT — font loads with `display: swap` behavior
- [ ] Fluid type scales smoothly from 320px to 1440px (drag browser width)
- [ ] At each breakpoint (480px, 768px, 1024px), type sizes are appropriate
- [ ] All notice types display correct border colors (info=cyan, warning=orange, success=green, danger=red, primary=purple)
- [ ] Date metadata displays in orange with mono font
- [ ] Scroll animations work in Chrome/Edge (CSS `animation-timeline` supported)
- [ ] In Firefox/Safari, archive items are visible normally (no invisible content)
- [ ] Page content `fadeInUp` stagger works on load
- [ ] Hero title shows gradient sweep animation
- [ ] Noise grain overlay is barely perceptible — adds texture without harming readability
- [ ] Secondary purple glow visible in bottom-right corner
- [ ] Grid lines at 5% opacity — present but not distracting
- [ ] Floating gradient orb visible behind hero area
- [ ] Blockquote decorative quotes visible but subtle (12% opacity)
- [ ] Hero diagonal clip-path creates clean angular divider
- [ ] Favicon appears in browser tab (SVG version)
- [ ] Print preview: white background, no decorative elements, no animations
- [ ] External link arrow `↗` does NOT appear on nav links
- [ ] Blog post disclaimer note renders correctly
- [ ] `/blog/` returns 404 (legacy files removed)
- [ ] Lighthouse performance audit: no regressions from new CSS
- [ ] All links in navigation still work
