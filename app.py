from flask import Flask, jsonify, render_template_string
import os
import socket
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

cache = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Lab</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #020617;
            color: white;
        }

        .page {
            max-width: 1000px;
            margin: auto;
            padding: 60px 20px;
        }

        .hero {
            text-align: center;
            padding: 60px 20px;
        }

        h1 {
            font-size: 70px;
            margin-bottom: 15px;
        }

        p {
            color: #cbd5e1;
            font-size: 20px;
        }

        .buttons a {
            display: inline-block;
            margin: 10px;
            padding: 14px 22px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            border-radius: 10px;
            font-weight: bold;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 18px;
            margin-top: 40px;
        }

        .card {
            background: #0f172a;
            padding: 25px;
            border-radius: 18px;
            border: 1px solid #1e293b;
        }

        .status {
            margin-top: 35px;
            background: #0f172a;
            padding: 25px;
            border-radius: 18px;
        }

        .status strong {
            color: #38bdf8;
        }
    </style>
</head>
<body>
    <div class="page">
        <div class="hero">
            <h1>DevOps Lab</h1>
            <p>Docker + Nginx + Flask + Redis project</p>

            <div class="buttons">
                <a href="/health" target="_blank">Health</a>
                <a href="/stats" target="_blank">Stats</a>
                <a href="/api" target="_blank">API</a>
            </div>
        </div>

        <div class="cards">
            <div class="card">
                <h2>Docker</h2>
                <p>Runs services in containers.</p>
            </div>

            <div class="card">
                <h2>Nginx</h2>
                <p>Works as reverse proxy.</p>
            </div>

            <div class="card">
                <h2>Flask</h2>
                <p>Python backend app.</p>
            </div>

            <div class="card">
                <h2>Redis</h2>
                <p>Stores visit counter.</p>
            </div>
        </div>

        <div class="status">
            <h2>Live Status</h2>
            <p>Visits: <strong>{{ visits }}</strong></p>
            <p>Container: <strong>{{ container }}</strong></p>
            <p>Redis host: <strong>{{ redis_host }}</strong></p>
        </div>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    visits = cache.incr("visits")

    return render_template_string(
        HTML_PAGE,
        visits=visits,
        container=socket.gethostname(),
        redis_host=REDIS_HOST
    )


@app.route("/api")
def api():
    visits = cache.get("visits") or 0

    return jsonify({
        "message": "Hello from Docker + Nginx + Flask + Redis",
        "visits": int(visits),
        "container": socket.gethostname()
    })


@app.route("/health")
def health():
    try:
        cache.ping()
        redis_status = "ok"
    except redis.exceptions.RedisError:
        redis_status = "error"

    return jsonify({
        "app": "ok",
        "redis": redis_status
    })


@app.route("/stats")
def stats():
    visits = cache.get("visits") or 0

    return jsonify({
        "total_visits": int(visits),
        "redis_host": REDIS_HOST,
        "app_container": socket.gethostname()
    })