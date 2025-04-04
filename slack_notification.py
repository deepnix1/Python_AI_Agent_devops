import requests
import os

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert(message):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

# Eğer log analizi sonucu anomali bulursa uyarı gönder
anomaly_result = analyze_logs()
if "anomaly" in anomaly_result.lower():
    send_alert(f"🚨 AI Log Analyzer: Anomali tespit edildi! \n\n{anomaly_result}")
