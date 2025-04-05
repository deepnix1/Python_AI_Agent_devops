from flask import Flask, Response
import logging
import os
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Loglama ayarları
if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    filename='logs/app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Prometheus metrikleri
REQUEST_COUNT = Counter('request_count', 'Total request count')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    app.logger.info("accessed ")
    return "Hello from AI DevOps!"

@app.route("/error")
def error():
    REQUEST_COUNT.inc()
    app.logger.error("simulation failed")
    return "mistake ", 500

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
