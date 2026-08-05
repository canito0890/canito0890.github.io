# AGENTS.md - Coding Guidelines for Joel Cano's Website

This is a Jekyll-based personal blog and résumé site hosted on GitHub Pages using the Minimal Mistakes theme.

## Build Commands

Ruby 3.4.1 is required and is selected by `.mise.toml` (not `.ruby-version` — mise
ignores that file unless ruby is added to `idiomatic_version_file_enable_tools`).
Run `mise trust && mise install` once; without the right Ruby, `bundle exec jekyll`
resolves against the system Ruby and fails with "command not found: jekyll".

```bash
# Install dependencies
bundle install

# Serve locally (auto-regenerates on changes)
bundle exec jekyll serve

# Serve with drafts and future posts
bundle exec jekyll serve --drafts --future

# Build site (outputs to _site/)
bundle exec jekyll build

# Build for production
JEKYLL_ENV=production bundle exec jekyll build

# Clean build cache
bundle exec jekyll clean

# Regenerate the résumé PDF and .docx from _data/resume.yml
bin/build-resume
```

## Project Structure

```
├── _config.yml           # Site configuration
├── _data/navigation.yml  # Navigation menu
├── _data/resume.yml      # Résumé source of truth (no contact details — see below)
├── _includes/resume/     # Résumé partials shared by the web page and the PDF
├── _layouts/resume-print.html  # Standalone print layout used to make the PDF
├── _pages/               # Static pages (About, Résumé, 404, archives)
├── _posts/               # Blog posts (YYYY-MM-DD-title.markdown)
├── _resume/              # Résumé tooling (docx generator + pandoc style template)
├── assets/css/main.scss  # Custom styles
├── assets/files/         # Public downloads, incl. the résumé PDF
├── bin/build-resume      # Regenerates the PDF and .docx
├── index.markdown        # Homepage
└── Gemfile               # Ruby dependencies
```

## Résumé

`_data/resume.yml` is the single source of truth for `/resume/`, the public PDF, the
private PDF, and the editable `.docx`. Never hand-edit the generated artifacts —
edit the YAML and run `bin/build-resume`.

Rules when touching résumé files:

- **No contact details in `_data/resume.yml`** — it is public in this repo. Email and
  phone live in `tmp/resume.private.yml` (gitignored) and reach only the private PDF
  and the `.docx`. `bin/build-resume` fails the build if the email hits public output.
- **Keep the two page sources in sync.** `_pages/resume.md` (themed) and
  `_pages/resume-print.html` (PDF) must include the same partials in the same order.
- **`_layouts/resume-print.html` must stay self-contained** — all CSS inline, system
  fonts only. It is rendered from a `file://` URL where external stylesheets and
  webfonts silently fail to load.
- `_pages/resume-print.html` is `published: false` on purpose; only
  `jekyll build --unpublished` (which `bin/build-resume` uses) emits it.
- Commit `assets/files/joel-cano-resume.pdf` alongside any `_data/resume.yml` change,
  or the site will serve a stale résumé.

See README.md for the full pipeline description.

## Content Creation Guidelines

### New Blog Posts

Create files in `_posts/` following naming convention: `YYYY-MM-DD-title.markdown`

**Required front matter:**
```yaml
---
title: "Your Post Title"
date: YYYY-MM-DD
---
```

**Optional front matter:**
```yaml
categories: [category1, category2]  # Use for broad topics
tags: [tag1, tag2, tag3]            # Use for specific keywords
excerpt: "Short description"
toc: true                           # Enable table of contents
toc_label: "Contents"
toc_icon: "rocket"
header:
  overlay_color: "#333"
  overlay_filter: "0.5"
```

### New Pages

Create in `_pages/` or root directory with front matter:
```yaml
---
layout: single
title: "Page Title"
permalink: /custom-path/
author_profile: true
classes: wide
toc: true
---
```

### Navigation

Update `_data/navigation.yml` to add menu items:
```yaml
main:
  - title: "Page Name"
    url: /permalink/
```

## Code Style Guidelines

### Markdown

- Use ATX-style headers (`#`, `##`) not Setext
- Indent lists with 2 spaces
- Use fenced code blocks with language specifiers
- Include blank lines around block elements
- Prefer reference-style links for repeated URLs

### YAML (Front Matter & Config)

- Use 2-space indentation
- Quote strings with special characters
- Use arrays for lists: `[item1, item2]`
- Follow existing _config.yml structure

### SCSS/CSS

- Located in `assets/css/main.scss`
- Import theme first, then add custom styles
- Use CSS variables from theme: `var(--primary-color)`
- Group related styles together
- Include responsive breakpoints with `@media`
- Prefer `rem` and `em` over pixels for sizing

### Naming Conventions

- **Posts**: `YYYY-MM-DD-kebab-case-title.markdown`
- **Categories**: lowercase, hyphenated (e.g., `web-development`)
- **Tags**: lowercase, hyphenated (e.g., `javascript`, `best-practices`)
- **Files**: kebab-case for multi-word names
- **Images**: descriptive-kebab-case.jpg in `/assets/images/`

## Configuration Standards

### _config.yml

- Maintain existing structure and comments
- Update author section for bio/social changes
- Test changes locally (requires restart)
- Keep sensitive data out (no API keys)

### Plugins

Available plugins (in Gemfile):
- `github-pages` - GitHub Pages compatibility
- `jekyll-feed` - RSS feed
- `jekyll-include-cache` - Performance
- `jekyll-paginate` - Post pagination
- `jekyll-sitemap` - XML sitemap
- `jekyll-gist` - Embed gists
- `jemoji` - Emoji support

## Error Handling & Validation

### Before Committing

1. Test locally: `bundle exec jekyll serve`
2. Check for YAML syntax errors in front matter
3. Verify all internal links work
4. Ensure images exist in `/assets/images/`
5. Review in both desktop and mobile widths

### Common Issues

- **YAML errors**: Check indentation and special characters
- **Build failures**: Run `bundle exec jekyll clean` then rebuild
- **Missing pages**: Verify `permalink` in front matter
- **Style not applying**: Check SCSS syntax, restart server

## Deployment

- Auto-deploys on push to `master` branch
- Uses GitHub Pages with `github-pages` gem
- Production URL: https://canito0890.github.io
- Build output goes to `_site/` (gitignored)

## Theme Information

- **Theme**: Minimal Mistakes (remote: mmistakes/minimal-mistakes)
- **Skin**: dark (configurable in _config.yml)
- **Docs**: https://mmistakes.github.io/minimal-mistakes/docs/
- Do not create local theme files unless overriding specific components

## Copilot Instructions (Preserved)

This project has `.github/copilot-instructions.md` with detailed guidance on:
- Architecture and key components
- Development workflow
- Content creation patterns
- Theme customization
- Archive and navigation setup

Refer to that file for comprehensive project context.
