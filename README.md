# Joel Cano's Personal Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://canito0890.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red)](https://jekyllrb.com/)
[![Minimal Mistakes](https://img.shields.io/badge/Theme-Minimal%20Mistakes-blue)](https://mmistakes.github.io/minimal-mistakes/)

Personal website, blog, and résumé built with Jekyll and the Minimal Mistakes theme. A place to share thoughts on software development, technology, and continuous learning.

## 🚀 Features

- **Modern Design**: Clean, responsive layout using the Minimal Mistakes dark theme
- **Data-driven résumé**: One YAML file renders the web page, the PDF, and the editable `.docx`
- **Blog Posts**: Write and publish blog posts using Markdown
- **Navigation**: Easy-to-use navigation with post archives, categories, and tags
- **Search**: Built-in search functionality
- **SEO Optimized**: Meta tags, sitemap, and RSS feed
- **Social Integration**: Links to GitHub and LinkedIn
- **Code Highlighting**: Syntax highlighting for code blocks
- **Table of Contents**: Automatic TOC generation for long posts
- **Responsive**: Mobile-friendly design
- **Custom Styling**: Enhanced CSS for better user experience

## 🛠️ Local Development

### Prerequisites

- Ruby 3.4.1 — pinned in both `.ruby-version` and `.mise.toml`
- Bundler gem
- For the résumé pipeline only: [pandoc](https://pandoc.org) and Google Chrome

If you use [mise](https://mise.jdx.dev), run `mise trust && mise install` once. The
`.mise.toml` is what actually selects Ruby 3.4.1 — mise ignores `.ruby-version`
unless ruby is added to `idiomatic_version_file_enable_tools`, and without the
right Ruby, `bundle exec jekyll` resolves against the system Ruby and fails.

### Setup

1. Clone the repository:
```bash
git clone https://github.com/canito0890/canito0890.github.io.git
cd canito0890.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Serve the site locally:
```bash
bundle exec jekyll serve
```

4. Open your browser and navigate to `http://localhost:4000`

## 📄 Updating the résumé

`_data/resume.yml` is the single source of truth. It feeds four surfaces:

| Artifact | Path | Committed? |
| --- | --- | --- |
| Web page | `/resume/` | yes |
| Public PDF | `assets/files/joel-cano-resume.pdf` | yes |
| Private PDF (with email) | `tmp/joel-cano-resume-private.pdf` | no — `tmp/` is gitignored |
| Editable `.docx` | `tmp/Joel-Cano-Resume.docx` | no — `tmp/` is gitignored |

To make a change:

```bash
# 1. edit the data
$EDITOR _data/resume.yml

# 2. regenerate the PDF and .docx
bin/build-resume

# 3. commit the data and the public PDF
git add _data/resume.yml assets/files/joel-cano-resume.pdf
```

**Contact details.** `_data/resume.yml` deliberately contains no email or phone —
it is public in this repo. Those live in `tmp/resume.private.yml` (gitignored) and
are merged only into the private PDF and the `.docx`. `bin/build-resume` fails the
build if the email ever reaches the public output.

**How the artifacts are produced.** `_pages/resume-print.html` is a `published: false`
page that renders through `_layouts/resume-print.html`, a standalone light-themed
layout with all CSS inlined and no webfonts. The script builds it with
`jekyll build --unpublished` into a scratch directory and prints it to PDF with
headless Chrome. Chrome writes the PDF but does not exit on its own, so the script
waits for the file to stop growing and then stops it. The `.docx` comes from
`_resume/generate_docx_md.rb`, which emits pandoc markdown that pandoc converts
using `_resume/reference.docx` for styling.

`_resume/reference.docx` is a style-only template derived from the original Google
Docs export — it keeps the styles and embedded fonts but contains no personal data.
Regenerate it with:

```bash
python3 _resume/make_reference_docx.py tmp/Resume.docx _resume/reference.docx
```

The PDF is committed rather than built in CI: GitHub Pages' native builder (required
by `remote_theme`) cannot run Chrome, and the PDF only changes when
`_data/resume.yml` does.

### Creating New Posts

Create a new file in the `_posts` directory following the naming convention:
```
YYYY-MM-DD-title.markdown
```

Example post structure:
```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
categories: [category1, category2]
tags: [tag1, tag2, tag3]
toc: true
toc_label: "Contents"
---

Your content here...
```

## 📁 Project Structure

```
├── _config.yml          # Site configuration
├── _data/
│   └── navigation.yml   # Navigation menu
├── _pages/              # Static pages (About, Archives, etc.)
├── _posts/              # Blog posts
├── assets/
│   └── css/
│       └── main.scss    # Custom styles
├── index.markdown       # Homepage
└── README.md           # This file
```

## 🎨 Customization

### Theme Settings

The site uses the **dark** skin of Minimal Mistakes. To change it, edit `_config.yml`:
```yaml
minimal_mistakes_skin: dark # options: default, air, aqua, contrast, dark, dirt, neon, mint, plum, sunrise
```

### Author Profile

Update your bio and social links in `_config.yml` under the `author:` section.

### Custom CSS

Custom styles are in `assets/css/main.scss`. Add your own CSS at the bottom of this file.

## 📝 Writing Tips

- Use **front matter** to set post metadata (title, date, categories, tags)
- Enable **TOC** (`toc: true`) for longer posts
- Use **code blocks** with syntax highlighting
- Add **images** to `assets/images/` directory
- Use **categories** for broad topics and **tags** for specific keywords

## 🚢 Deployment

The site automatically deploys to GitHub Pages when you push to the `master` branch.

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Connect

- **Website**: [canito0890.github.io](https://canito0890.github.io)
- **GitHub**: [@canito0890](https://github.com/canito0890)

---

Built with ❤️ using [Jekyll](https://jekyllrb.com/) and [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/)
