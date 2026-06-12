from flask import Flask, jsonify
import os
import socket
import redis

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

cache = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)


@app.route("/")
def home():
    visits = cache.incr("visits")

    return jsonify({
        "message": "Hello from Docker + Nginx + Flask + Redis",
        "visits": visits,
        "container": socket.gethostname()
    })


@app.route("/health")
def health():
    try:
        cache.ping()
        redis_status = "ok"
    except redis.exceptions.ConnectionError:
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