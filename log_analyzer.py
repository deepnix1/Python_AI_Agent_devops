import openai
import os
from dotenv import load_dotenv
import requests

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def analyze_logs():
    with open("logs/app.log", "r") as file:
        log_data = file.read()

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI log analyzer. Look for any unusual or error patterns in the logs."},
            {"role": "user", "content": log_data}
        ]
    )

    return response.choices[0].message.content.strip()

def send_alert(message):
    payload = {"text": message}
    requests.post(SLACK_WEBHOOK_URL, json=payload)

# Anomali kontrolü
result = analyze_logs()
print("Analysis Result:", result)

if "anomaly" in result.lower() or "error" in result.lower():
    send_alert(f"🚨 AI Log Analyzer: Anomali tespit edildi! \n\n{result}")
