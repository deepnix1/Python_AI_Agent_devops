import requests
import os
from log_analyzer import analyze_logs

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_alert(message):
    payload = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, json=payload)
    print("Slack Response Status Code:", response.status_code)

# Log analizi sonucunu al ve ekrana yazdır
anomaly_result = analyze_logs()
print("Anomaly Result:", anomaly_result)

# Eğer log analizi sonucu anomali bulursa uyarı gönder
if "anomali" in anomaly_result.lower():
    send_alert(f"🚨 AI Log Analyzer: Anomaly detected! \n\n{anomaly_result}")
else:
    print("no anomaly detected")


send_alert(f"🚨 AI log analyzer : \n\n{anomaly_result}")