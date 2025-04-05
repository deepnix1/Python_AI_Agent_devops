import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Gemini API anahtarınızı ortam değişkeninden alıyoruz.
api_key = os.getenv("GEMINI_API_KEY")

# Google GenAI istemcisini API anahtarımızla başlatıyoruz.
client = genai.Client(api_key=api_key)

def analyze_logs():
    try:
        with open("logs/app.log", "r") as file:
            log_data = file.read()
    except FileNotFoundError:
        return "cant find log file"

    # Log verisini Gemini AI ile analiz etmek için isteği gönderiyoruz.
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"you are an AI analyzer.Please inform me of the things I need to change. If you detect any error or anomaly in the following logs, notify me.:\n\n{log_data}"
    )
    return response.text.strip()

if __name__ == "__main__":
    result = analyze_logs()
    print("Anomaly Analysis Result:", result)
