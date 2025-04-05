FROM python:3.9-slim

WORKDIR /app

# Gereksinim dosyasını kopyala ve paketleri yükle
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Tüm proje dosyalarını kopyala
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
