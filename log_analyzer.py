import openai
import os

# OpenAI API Anahtarı
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs():
    with open("logs/app.log", "r") as log_file:
        logs = log_file.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI that analyzes DevOps logs and detects anomalies."},
            {"role": "user", "content": f"Analyze these logs and find anomalies:\n{logs}"}
        ]
    )

    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    analysis_result = analyze_logs()
    print("Anomaly Analysis Result:", analysis_result)
