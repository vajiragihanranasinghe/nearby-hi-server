from flask import Flask, request, jsonify
import os

app = Flask(__name__)

messages = []  # temporary memory

@app.route("/")
def home():
    return "Nearby Hi server running ✅"

@app.route("/hi", methods=["POST"])
def say_hi():
    data = request.json
    name = data.get("name", "Unknown")
    msg = f"👋 Hi from {name}"
    messages.append(msg)
    return jsonify({"status": "ok", "message": msg})

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
