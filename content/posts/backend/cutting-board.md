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