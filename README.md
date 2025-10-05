# Joel Cano's Personal Website

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-brightgreen)](https://canito0890.github.io)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.x-red)](https://jekyllrb.com/)
[![Minimal Mistakes](https://img.shields.io/badge/Theme-Minimal%20Mistakes-blue)](https://mmistakes.github.io/minimal-mistakes/)

Personal website and blog built with Jekyll and the Minimal Mistakes theme. A place to share thoughts on software development, technology, and continuous learning.

## 🚀 Features

- **Modern Design**: Clean, responsive layout using the Minimal Mistakes dark theme
- **Blog Posts**: Write and publish blog posts using Markdown
- **Navigation**: Easy-to-use navigation with post archives, categories, and tags
- **Search**: Built-in search functionality
- **SEO Optimized**: Meta tags, sitemap, and RSS feed
- **Social Integration**: Links to GitHub, email, and other social profiles
- **Code Highlighting**: Syntax highlighting for code blocks
- **Table of Contents**: Automatic TOC generation for long posts
- **Responsive**: Mobile-friendly design
- **Custom Styling**: Enhanced CSS for better user experience

## 🛠️ Local Development

### Prerequisites

- Ruby (version 2.7 or higher)
- Bundler gem

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
