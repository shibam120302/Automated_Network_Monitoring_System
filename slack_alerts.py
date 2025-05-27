# slack_alerts.py
# Sends alert to a Slack channel using Incoming Webhook

import requests

def send_slack_alert(message):
    url = "https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK"
    payload = {"text": message}
    try:
        response = requests.post(url, json=payload)
        if response.status_code != 200:
            print("Slack error:", response.text)
    except Exception as e:
        print(f"Slack alert failed: {e}")
