---
title: "Setting Up This Website"
date: "2023-11-24"
category: "tech"
---

Server & Docker Setup
	•	Set up a Debian VPS for hosting multiple projects.
	•	Installed Docker and Docker Compose on the VPS.
	•	Cloned your Git repository containing the Docker files for the demo app.
	•	Built and ran the Docker containers using docker-compose up --build -d.
	•	Verified that the API and PostgreSQL containers were running.
	•	Confirmed the API was serving requests internally (via curl and logs).

⸻

Domain & DNS
	•	Verified that your main domain (v01dworks.com) resolves to your VPS.
	•	Created an A record for the subdomain demo.v01dworks.com pointing to the VPS IP.
	•	Tested DNS propagation (ping demo.v01dworks.com) to confirm it resolves correctly.

⸻

Nginx Reverse Proxy
	•	Installed Nginx on the VPS.
	•	Created a new server block in /etc/nginx/sites-available/demo.v01dworks.com for the subdomain.
	•	Configured the server block as a reverse proxy pointing to the Docker container (API on port 8000).
	•	Enabled the site with a symlink in /etc/nginx/sites-enabled/.
	•	Tested Nginx configuration and reloaded the service.
	•	Verified that http://demo.v01dworks.com correctly forwards to your Docker app.

⸻

Tools / Utilities
	•	Installed tmux to manage long-running terminal sessions.
	•	Confirmed Docker containers stay up and logs can be viewed while detached.

⸻

Next Planned Steps
	•	Set up Certbot to issue a free SSL certificate for demo.v01dworks.com.
	•	Configure automatic HTTPS redirection via Nginx.
	•	Plan for multiple Docker containers with different subdomains (e.g., main site, demo app, future projects).
