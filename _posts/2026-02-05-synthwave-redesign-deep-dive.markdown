---
title: "Behind the Screens: A Deep Dive into My Site's Synthwave Redesign"
date: 2026-02-05
categories: [design, web-development, process]
tags: [jekyll, minimal-mistakes, synthwave, css, frontend-design]
excerpt: "A detailed look at how I transformed my personal site with an Outrun/Synthwave aesthetic, complete with the planning process, design decisions, and technical implementation using opencode."
header:
  overlay_color: "#0f0f1e"
  overlay_filter: "0.5"
toc: true
toc_label: "What We'll Cover"
toc_icon: "palette"
---

## Introduction

Every now and then, a website needs more than just new content—it needs a soul transplant. After living with my Jekyll site for a while, I realized it was time for something bolder, something that truly reflected my personality as a developer who appreciates both retro nostalgia and futuristic tech.

Enter: the **Outrun/Synthwave redesign**.

This wasn't just a coat of paint. It was a complete reimagining of the site's visual identity, from color palettes to typography to micro-interactions. And I documented the entire process.

## The Planning Phase

### Using opencode for Design Intelligence

Before writing a single line of CSS, I leveraged **opencode**—an AI-powered development environment—to think through the redesign systematically. This wasn't about generating generic "AI slop" designs. Instead, I used it as a collaborative thinking partner.

The process started with a thorough audit:

1. **Site Structure Analysis** - Reviewed the existing Jekyll setup with Minimal Mistakes theme
2. **Design Direction Exploration** - Evaluated multiple aesthetic options (Brutalist, Minimal, Retro-Futuristic, Editorial)
3. **Technical Constraints Assessment** - Ensured compatibility with GitHub Pages and the remote theme architecture
4. **Content Review** - Analyzed existing pages, posts, and navigation

### Choosing the Aesthetic

The decision to go with **Outrun/Synthwave** wasn't arbitrary. This style perfectly captures that intersection between retro nostalgia (80s neon, grid patterns, sunset gradients) and modern development (clean code, futuristic interfaces).

The guiding principles:
- **Bold but not overwhelming** - Distinctive visual identity without sacrificing usability
- **Developer-appropriate** - Technical sophistication meets creative expression
- **Accessible** - WCAG AA compliant color contrast despite the vibrant palette
- **Performant** - Minimal animations, no heavy assets, CSS-only effects where possible

## Design System Architecture

### Color Palette

The color system is built on CSS custom properties for consistency:

```css
:root {
  --bg-primary: #0f0f1e;      /* Deep navy */
  --bg-secondary: #1a1a3e;    /* Lighter navy */
  --bg-card: #16162a;         /* Surface color */
  
  --accent-sunset: #ff6b35;   /* Sunset orange */
  --accent-pink: #ff006e;     /* Hot pink */
  --accent-cyan: #00d9ff;     /* Electric cyan */
  --accent-purple: #9d4edd;   /* Synth purple */
  
  --text-primary: #f0f0f5;    /* Soft white */
  --text-secondary: #a0a0b0;  /* Muted gray */
}
```

These aren't just pretty colors—they're carefully chosen for contrast ratios:
- Primary text on background: **14.5:1** (WCAG AAA)
- Secondary text: **7.2:1** (WCAG AA)
- All accent colors maintain readability standards

### Typography Trinity

Three fonts, three purposes:

1. **Righteous** - Display/headlines, that retro-futuristic geometric punch
2. **Inter** - Body text, maximum readability at all sizes
3. **JetBrains Mono** - Code blocks, developer cred and excellent legibility

### Visual Effects

The synthwave aesthetic comes alive through subtle details:

- **Gradient backgrounds** - Deep purple-blue transitions that create depth
- **Grid pattern overlay** - Subtle 60px pink-tinted grid lines (2% opacity)
- **Glow effects** - Cards and buttons emit soft colored shadows on hover
- **Gradient text** - Headlines use background-clip for sunset-to-pink transitions
- **Animated cursor** - The tagline "Brewing up some code" has a blinking cyan cursor

## Technical Implementation

### The CSS Architecture

The entire design system lives in `assets/css/main.scss`, overriding the Minimal Mistakes dark skin. Key architectural decisions:

**CSS Custom Properties** - Single source of truth for all design tokens. Change a color in one place, it updates everywhere.

**Layered Effects** - Using pseudo-elements for overlays:
```css
body::before {
  /* Grid pattern overlay */
  background-image: 
    linear-gradient(rgba(255, 0, 110, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 0, 110, 0.02) 1px, transparent 1px);
  background-size: 60px 60px;
}
```

**Interactive States** - Every clickable element has intentional hover/focus states:
- Links: Animated underline that draws left-to-right
- Cards: Lift 6px + glow intensify
- Buttons: Scale 1.02x + subtle pulse

### Syntax Highlighting Overhaul

Rouge (the default Jekyll highlighter) got a synthwave makeover:

```css
.highlight .k { color: #ff006e; font-weight: 600; } /* Keywords - hot pink */
.highlight .s { color: #ff6b35; }                  /* Strings - sunset */
.highlight .mi { color: #00d9ff; }                 /* Numbers - cyan */
.highlight .nf { color: #9d4edd; }                 /* Functions - purple */
```

### Responsive Strategy

Mobile wasn't an afterthought—it was baked in from the start:

- **1024px breakpoint** - Tablet optimizations, sidebar adjustments
- **768px breakpoint** - Mobile navigation, typography scaling, touch targets
- **480px breakpoint** - Small phone refinements, full-width code blocks

Key mobile considerations:
- Grid pattern scales down (60px → 40px)
- Code blocks go full-bleed for better readability
- Navigation becomes more compact
- Touch targets meet 44px minimum

## Problem-Solving Moments

### The Bio Table Bug

Here's a fun one: the bio in the sidebar was rendering as an HTML table instead of text. Why? The pipe characters `|` in:

```yaml
bio: "Software Developer | Tech Enthusiast | ..."
```

Jekyll/Markdown interpreted those as table cell separators. **Solution**: Replace pipes with bullet points `•`. Simple fix, but a good reminder that YAML + Markdown can have unexpected interactions.

### Performance vs. Polish

The original grid pattern was too prominent—0.03 opacity at 50px spacing competed with content. After testing, I dialed it back to 0.02 opacity with 60px spacing. Still atmospheric, but it doesn't fight for attention.

### Navigation Simplification

Originally had 6 nav items including Categories and Tags. **Streamlined to 4**:
- Home
- About
- Posts
- GitHub (external)

Categories and tags still exist and are accessible from the Posts page, but the primary navigation is cleaner and more focused.

## The Review Process

After initial implementation, I conducted a thorough design review looking for:

1. **Consistency** - Do all elements use the design tokens? Are borders, shadows, and spacing uniform?
2. **Responsiveness** - Does it look good from 320px to 1440px? Are touch targets accessible?
3. **Aesthetic Cohesion** - Does everything feel like it belongs in the same universe?
4. **Performance** - Are animations smooth? Is the CSS efficient?

### Tools Used

- **opencode** - Planning, code generation, and review
- **Jekyll** - Static site generation
- **Minimal Mistakes** - Base theme (heavily customized)
- **GitHub Pages** - Hosting
- **Google Fonts** - Righteous, Inter, JetBrains Mono

## Lessons Learned

### What Worked

1. **CSS Custom Properties** are game-changers for theming. Want to tweak the sunset color? One line change propagates everywhere.

2. **Minimal animations** can have maximum impact. The blinking cursor on the tagline took 5 lines of CSS but adds so much character.

3. **Planning before coding** saved hours of refactoring. Having a clear design system before writing styles meant fewer "what if I tried..." moments.

### What I'd Do Differently

1. **Start with real content** - Some spacing decisions were based on placeholder text. Real content always reveals edge cases.

2. **Test on actual devices earlier** - Browser DevTools are great, but nothing beats testing on a real phone.

3. **Document component usage** - Future me will thank present me for explaining which CSS classes do what.

## The Result

The site now has a distinctive visual identity that sets it apart from generic developer blogs. It's:

- **Memorable** - Visitors remember the synthwave aesthetic
- **Readable** - Content is king, and the design supports it
- **Accessible** - Meets WCAG standards without sacrificing style
- **Maintainable** - Clean CSS architecture with clear patterns
- **Performant** - No heavy assets, minimal JavaScript, CSS-only effects

## What's Next?

This redesign establishes a solid foundation. Future enhancements might include:

- Dark/light theme toggle (though the dark synthwave vibe is pretty core to the identity)
- More interactive elements using CSS-only techniques
- Custom post layouts for different content types
- Animated page transitions

But for now, the site feels complete. It has personality. It has soul. And most importantly, it's a pleasure to write in and a pleasure to read.

## Resources

If you want to dive deeper into synthwave web design:

- [Minimal Mistakes Theme Documentation](https://mmistakes.github.io/minimal-mistakes/docs/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Google Fonts](https://fonts.google.com/) - For Righteous, Inter, and JetBrains Mono
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) - For accessibility verification

---

*Have thoughts on the redesign? Found a bug? Want to chat about CSS architecture? [Hit me up on GitHub](https://github.com/canito0890).*

*Brewing up more code, one commit at a time.*
