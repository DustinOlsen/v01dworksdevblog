---
title: "Making a GameDev Asset Catalogue"
date: "2025-11-24"
category: "backend"
---

# The Concept
* Game Dev Asset Catalogue: A centralized, web-based management system designed for game developers to organize, store, and retrieve assets (textures, 3D models, audio files, and scripts).
* Problem Solved: Replaces disorganized local folders with a searchable, tagged, and categorized database accessible via a web interface.
# The Tech Stack
* Backend: Built with FastAPI (Python 3.11) for high-performance, asynchronous REST API endpoints.
* Database: Uses PostgreSQL for robust relational data storage, managed via SQLAlchemy ORM.
* Frontend: A lightweight, responsive interface built with Vanilla JavaScript, HTML5, and CSS3 (no heavy frontend frameworks required).
* Containerization: Fully Dockerized using Docker and Docker Compose to orchestrate the API and Database services, ensuring consistent environments from development to production.
# Key Features
* Secure Authentication: Implements JWT (JSON Web Tokens) for stateless authentication and uses pbkdf2_sha256 for secure password hashing.
* Asset Management (CRUD): Full capability to upload, view, search, and delete assets.
* File Handling: Handles multipart file uploads, storing physical files on the server while maintaining metadata references in the database.
* Smart Seeding: Includes an auto-seeding feature that populates the database with demo data for the test user upon first login.
* User Isolation: Enforces strict data ownership—users can only view and manage assets they personally uploaded.
Portfolio-Specific Features
* Demo Mode: A specialized configuration that disables public registration and provides a pre-filled "Test User" login
, allowing recruiters and visitors to test the application immediately without friction.
* Production Ready: Configured with environment variables (.env) to easily switch between development (debug mode) and production security settings.
