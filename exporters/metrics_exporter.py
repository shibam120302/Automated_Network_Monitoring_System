# exporters/metrics_exporter.py
# Prometheus metrics exporter

from prometheus_client import Gauge, start_http_server

# Define Prometheus metric
packet_loss_gauge = Gauge('network_packet_loss', 'Packet loss status per device', ['device_ip'])

# Start metrics server
start_http_server(8000)

# Update metric value (1 = loss, 0 = OK)
def update_metrics(ip, status):
    packet_loss_gauge.labels(device_ip=ip).set(0 if status else 1)
