# 📦 Changelog - Portfólio Back-Office Django
**Project deployed to Render using Docker and Render YAML**  
**Date:** 2025-04-29

---

## ✨ Features

### [`activity_log`]
- Add app to register and track user activity
- Limit stored activities to 20 for performance in free-tier deployments
- JWT-protected access only

### [`support_requests`]
- Add app to collect and manage support or contact messages
- Auto-delete oldest entry when over 20 entries
- Admin panel support with status resolution

### [`users`]
- Implement custom User model with `email` as the login field
- JWT authentication using email/password
- `UserViewSet` with password handling and 5-user cap
- Add `/me/` endpoint to return authenticated user info

---

## 🛠 Configuration & Structure

### [`config`]
- Cleaned up `urls.py` with tags for Swagger separation
- Token routes moved under `/auth/`
- Swagger `/docs` organized into: Users, Auth, Support, Activity

### [`static`]
- Introduced animated typing message and branding logo

---

## 🧪 API Improvements

- All ViewSets include tags and descriptions for Swagger
- JWT token acquisition and usage clearly documented
- `/auth/token/` and `/auth/token/refresh/` fully working

---

## 🐳 Deploy-ready

- Ready for Docker & Render deploy with volume-free SQLite structure
- Follows Render free-tier resource constraints (limited users/logs)
