# monitor.py
# Main monitoring script to ping devices, check status, send alerts, and trigger remediation.

from netmiko import ConnectHandler
import subprocess
import time
from slack_alerts import send_slack_alert
from email_alerts import send_email_alert
from exporters.metrics_exporter import update_metrics

# List of network devices to monitor
devices = [
    {"host": "192.168.1.1", "username": "admin", "password": "admin", "device_type": "cisco_ios"},
    {"host": "192.168.1.2", "username": "admin", "password": "admin", "device_type": "cisco_ios"},
]

# Ping the device and check for packet loss
def ping_device(ip):
    result = subprocess.run(["ping", "-c", "3", ip], capture_output=True, text=True)
    return "0% packet loss" in result.stdout

# Remediation function using Netmiko to restart router/service
def remediate(device):
    try:
        conn = ConnectHandler(**device)
        output = conn.send_command("reload")  # Replace with actual restart command
        print(f"Remediated: {device['host']}")
        return output
    except Exception as e:
        print(f"Remediation failed: {e}")

# Continuous monitoring loop
def monitor_loop():
    while True:
        for device in devices:
            ip = device["host"]
            status = ping_device(ip)
            update_metrics(ip, status)  # Update Prometheus metrics
            if not status:
                msg = f"ALERT: {ip} is down or has high latency."
                print(msg)
                send_slack_alert(msg)
                send_email_alert("Network Alert", msg)
                remediate(device)
            else:
                print(f"{ip} is healthy.")
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    monitor_loop()
