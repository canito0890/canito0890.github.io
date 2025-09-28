# AI Coding Instructions for Joel Cano's Personal Website

## Project Overview
This is a Jekyll-based personal website/blog hosted on GitHub Pages using the **Minimal Mistakes** remote theme with dark skin. The site structure follows Jekyll conventions with posts, configuration, and theme customization.

## Architecture & Key Components

### Core Configuration
- **`_config.yml`**: Central configuration file defining site metadata, theme settings, author info, and plugin configuration
- **Remote theme**: Uses `mmistakes/minimal-mistakes` - avoid creating local theme files unless overriding specific components
- **Plugins**: Key plugins include `jekyll-feed`, `jekyll-paginate`, `jekyll-sitemap`, and GitHub Pages compatibility

### Content Structure
- **Posts**: Located in `_posts/` following `YYYY-MM-DD-title.markdown` naming convention
- **Pages**: Can be added to `_pages/` directory (configured in `_config.yml` includes)
- **Home layout**: `index.markdown` uses `layout: home` which displays recent posts automatically

### Author & Navigation
- Author profile configured in `_config.yml` with bio, avatar, and social links
- Footer and header links defined in configuration
- Default layouts set per content type (posts use `single` layout with author profile, read time, comments, etc.)

## Development Workflow

### Local Development
```bash
# Install dependencies
bundle install

# Serve locally with live reload
bundle exec jekyll serve

# Build site
bundle exec jekyll build
```

### Content Creation Patterns
1. **New blog posts**: Create in `_posts/` with proper front matter:
   ```yaml
   ---
   title: "Post Title"
   date: YYYY-MM-DD
   categories: [category1, category2]  # optional
   tags: [tag1, tag2]  # optional
   ---
   ```

2. **New pages**: Create in `_pages/` or root with front matter specifying layout and permalink

### GitHub Pages Deployment
- Automatic deployment on push to `master` branch
- Uses `github-pages` gem for compatibility
- Built site outputs to `_site/` (excluded from version control)

## Project-Specific Conventions

### Theme Customization
- Uses `minimal_mistakes_skin: dark` for consistent styling
- Author profile enabled by default on posts and pages
- Search functionality enabled (`search: true`)
- Pagination set to 5 posts per page

### Permalink Structure
- Posts use `/:categories/:title/` permalink structure
- Generates clean URLs without dates in path

### Asset Management
- Theme assets managed by remote theme
- Custom assets should go in `assets/` directory
- Avatar image expected at `/assets/images/bio-photo.jpg`

### Archives & Navigation
- Category and tag archives use liquid templates
- Automatic sitemap and feed generation via plugins
- Include cache plugin optimizes build performance

## Key Files to Modify
- **`_config.yml`**: Site settings, author info, theme configuration
- **`_posts/*.markdown`**: Blog content
- **`index.markdown`**: Homepage configuration
- **`Gemfile`**: Ruby dependencies (rarely modified)
- **`README.md`**: Project documentation

## Common Tasks
- Adding posts: Create in `_posts/` with proper naming and front matter
- Updating author info: Modify author section in `_config.yml`
- Changing theme settings: Update `_config.yml` theme configuration
- Adding pages: Create in root or `_pages/` with appropriate front matter