# DevOps Lab Site

A mini DevOps project with Docker, Nginx, Python Flask, Redis and Gunicorn.

## Stack

- Python
- Flask
- Redis
- Docker
- Docker Compose
- Nginx
- Gunicorn

## What this project does

This project runs a Flask website inside Docker.

Nginx works as a reverse proxy.

Redis stores a live visit counter.

Docker Compose starts all services together.

## Architecture

Browser -> Nginx -> Flask -> Redis

## How to run

```bash
docker compose up --build

Open in browser:

http://localhost:8081
Endpoints

Home page:

/

JSON API:

/api

Health check:

/health

Stats:

/stats
What I learned
How to build a Flask web app
How to use Redis with Python
How to run multiple services with Docker Compose
How to use Nginx as a reverse proxy
How to prepare a project for GitHub

Сохрани.

---

## 4. Проверь файлы

В PowerShell:

```powershell
cd C:\Users\veliki\Desktop\devops-lab-site
dir