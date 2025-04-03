from flask import Flask, request
import logging

app = Flask(__name__)

# Log dosyası konfigürasyonu
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/")
def home():
    app.logger.info("Ana sayfa erişildi.")
    return "Hello from AI DevOps!"

@app.route("/error")
def error():
    app.logger.error("Simüle edilen hata meydana geldi!")
    return "Hata oluştu!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
