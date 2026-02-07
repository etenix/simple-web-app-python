from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "SimpleApp")
DEBUG = os.getenv("DEBUG", "False") == "True"
PORT = int(os.getenv("PORT", 5000))


@app.route("/")
def home():
    return f"Welcome to {APP_NAME}!"


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/info")
def info():
    return jsonify(
        app_name=APP_NAME,
        debug=DEBUG,
        port=PORT
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)