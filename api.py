# api.py
# Exposes a simple Flask API to check device status via HTTP

from flask import Flask, jsonify
from monitor import ping_device

app = Flask(__name__)

@app.route("/status/<ip>")
def status(ip):
    alive = ping_device(ip)
    return jsonify({"ip": ip, "status": "up" if alive else "down"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
