# v01dworks.com

The source code for [v01dworks.com](https://v01dworks.com), a personal portfolio and blog network built with a custom static site generator.

## 🚀 Overview

This project is a monorepo-style structure containing the main landing page and a unified blog application. Instead of using a heavy CMS or framework like Next.js or Hugo, I built a custom Python-based static site generator to compile Markdown content into a lightweight, fast-loading site.

## 🛠 Tech Stack

- **Frontend:** Vanilla HTML5, CSS3, JavaScript (No frameworks)
- **Build System:** Python 3.11+
- **Content:** Markdown with Frontmatter
- **Styling:** Custom CSS with native Light/Dark mode support

## 📂 Project Structure

```text
├── apps/               # Web applications
│   ├── home/           # Main landing page (v01dworks.com)
│   └── blogs/          # Blog template for subdomains (backend., tech., etc.)
├── content/            # Markdown content source
│   ├── posts/          # Blog posts organized by category
│   └── about.md        # About page content
├── scripts/            # Build tools
│   └── generate_index.py # Generates posts.json from Markdown files
└── README.md
```

## 🔧 Usage

### Adding Content
1. Create a new Markdown file in `content/posts/<category>/`.
2. Ensure it has the required frontmatter:
   ```yaml
   ---
   title: "Your Post Title"
   date: "YYYY-MM-DD"
   category: "backend" # or tech, ios, etc.
   excerpt: "A short summary..."
   ---
   ```

### Building the Site
Run the generator script to parse all markdown files and update the `posts.json` index used by the frontend.

```bash
python3 scripts/generate_index.py
```

## 🌐 Routing & Categories

The site uses a single blog application (`apps/blogs`) that dynamically filters content based on URL query parameters. This allows for distinct "blog" experiences without needing separate deployments or subdomains.

- **Main Site:** `v01dworks.com` → `apps/home`
- **Backend Blog:** `v01dworks.com/blogs/?category=backend`
- **Tech Blog:** `v01dworks.com/blogs/?category=tech`



## 📄 License

© 2025 Dustin Olsen. All Rights Reserved.
