# Docker Flask Redis Nginx Project

Small backend project built with Python Flask, Redis, Docker Compose and Nginx.

## Stack

* Python
* Flask
* Redis
* Docker
* Docker Compose
* Nginx
* Gunicorn

## What this project does

This project runs a Python Flask API inside Docker.
Nginx works as a reverse proxy.
Redis stores a visit counter.
Docker Compose starts all services together.

## Architecture

Browser → Nginx → Flask App → Redis

## Endpoints

### Home

GET /

Returns message, visit counter and container name.

### Health

GET /health

Checks if Flask app and Redis are working.

### Stats

GET /stats

Shows total visits and Redis connection info.

## How to run

```bash
docker compose up --build
```

Open in browser:

```text
http://localhost:8080
```

Health check:

```text
http://localhost:8080/health
```

Stats:

```text
http://localhost:8080/stats
```

## Useful commands

Stop project:

```bash
docker compose down
```

Show running containers:

```bash
docker ps
```

Show logs:

```bash
docker compose logs -f
```

Rebuild project:

```bash
docker compose up --build
```

## What I learned

* How to containerize a Python Flask app
* How to use Redis with Python
* How Docker Compose connects multiple services
* How Nginx works as a reverse proxy
* How to expose only Nginx to the host machine
* How to use persistent Redis volume
* How to prepare a project for GitHub
