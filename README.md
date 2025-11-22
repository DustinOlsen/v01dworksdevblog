# v01dworks DevBlog

This project is a monorepo containing the personal website and devblogs for v01dworks.

## Structure

The project is organized to support multiple subdomains and a custom backend.

### Apps (`/apps`)

- **`home`**: The main landing page (`v01dworks.com`).
- **`blogs`**: A unified blog application that serves content for the different subdomains (`backend.v01dworks.com`, `gamedev.v01dworks.com`, etc.).
    - Alternatively, this can be split into separate apps if the designs diverge significantly.

### Backend (`/backend`)

- **`api`**: The custom backend API (Node.js, Python, Go, etc.) that serves blog posts, project data, and other dynamic content.

### Content (`/content`)

- **`posts`**: Markdown/MDX files for blog posts, organized by category.
    - `/backend`
    - `/gamedev`
    - `/ios`
    - `/tech`

## Subdomains

- `v01dworks.com` -> `apps/home`
- `backend.v01dworks.com` -> `apps/blogs` (filtered by 'backend' category)
- `gamedev.v01dworks.com` -> `apps/blogs` (filtered by 'gamedev' category)
- `ios.v01dworks.com` -> `apps/blogs` (filtered by 'ios' category)
- `tech.v01dworks.com` -> `apps/blogs` (filtered by 'tech' category)
