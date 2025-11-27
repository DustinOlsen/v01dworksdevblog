---
title: "Cutting Board - a Recipe Library App"
date: "2025-11-24"
category: "backend"
---

# Project Name: CuttingBoard
A personal recipe manager and kitchen assistant.

# Core Features:
* Recipe Management: Create, edit, and organize recipes. Includes a dynamic form interface for adding ingredients line-by-line.
* Smart Pantry Integration: The app automatically cross-references recipe ingredients with your pantry inventory.
* Visual Indicators: Ingredients you have are marked with a green checkmark; missing items show a cart icon.
* Shopping List Workflow: One-click "Add to Cart" functionality directly from the recipe view for missing ingredients.
* User Isolation: Full multi-user support where recipes, pantry items, and shopping lists are private to each account.
# Tech Stack:
* Backend: Python 3.11+, FastAPI, Uvicorn.
* Database: PostgreSQL with SQLAlchemy ORM.
* Frontend: Server-side rendering with Jinja2, enhanced by Vanilla JavaScript (ES6+) for dynamic interactivity (no heavy frameworks like React/Vue).
* Styling: Custom CSS3 with CSS Variables for native Light/Dark mode support.
* Authentication: OAuth2 with Password Flow and JWT (JSON Web Tokens) for stateless session management.
# Key Architectural Decisions:
* Unified Item Model: Instead of storing ingredients as simple text strings, they are stored as unique Item entities in the database. This allows the system to
intelligently link a "Tomato" in a recipe to a "Tomato" in your pantry or shopping list.
* Dynamic DOM Manipulation: The frontend uses raw JavaScript to handle complex form interactions (like adding/removing ingredient rows) and intercepts form submissions to format data cleanly for the API.

# Infrastructure & Deployment
* VPS Setup: Configured Docker Compose to orchestrate the web app, database, and Nginx reverse proxy.

* Static Files:
    * Problem: 404 errors and "Mixed Content" warnings (loading HTTP assets on an HTTPS site).
    * Fix: Switched from FastAPI's url_for (which generated absolute HTTP URLs behind the proxy) to relative paths (e.g., /static/css/...) in Jinja2 templates.
* Docker Production Workflow:
    * Problem: Code changes (like the mobile menu) weren't appearing on the VPS after pulling git changes.
    * Fix: Realized production Docker setup copies files into the image rather than mounting volumes. Used docker-compose up -d --build to force a rebuild of the container with the new code.
Database Troubleshooting
* Migration Errors:
    * Problem: relation "user" does not exist errors during startup.
    * Root Cause: The initial Alembic migration file was empty/desynchronized from the actual models.
    * Fix: Performed a "hard reset" by wiping the Docker volumes (docker-compose down -v), deleting old migration versions, and regenerating a fresh migration with alembic revision --autogenerate.
* Dependency Conflict:
    * Problem: passlib threw errors regarding bcrypt hashing.
    * Fix: Downgraded bcrypt to version 4.0.1 in requirements.txt to resolve compatibility issues.
# Frontend & Mobile Polish
* Hamburger Menu:
    * Implemented a responsive navigation bar that collapses into a hamburger menu on screens smaller than 1024px.
    * Used vanilla JavaScript to toggle an .active class for the menu slide-out effect.
* The "Giant Checkbox" Bug:
    * Problem: The "Show only what I can make" checkbox on the search bar was rendering full-width, breaking the mobile layout.
    * Root Cause: A global CSS rule input { width: 100%; } intended for text fields was accidentally targeting checkboxes too.
    * Fix: Added a specific override: input[type="checkbox"] { width: auto; }.
* Cache Busting:
    * Problem: CSS updates weren't showing up on mobile devices due to aggressive browser caching.
    * Fix: Appended a version query parameter (?v=1.6) to the stylesheet link in base.html to force browsers to fetch the new file.