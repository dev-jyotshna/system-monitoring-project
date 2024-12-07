import psutil
import time
from prometheus_client import start_http_server, Gauge
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

LOG_FILE = "system_logs.txt"
CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 80 
DISK_PATH = "C:"

cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage Percentage')
memory_usage_gauge = Gauge('memory_usage', 'Memory Usage Percentage')
disk_usage_gauge = Gauge('disk_usage', 'Disk Usage Percentage')

def send_email(subject, body):
    """Send email alerts."""
    try:
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message)
            print(f"Email sent: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def log_event(message):
    """Log events to a file."""
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{time.ctime()}: {message}\n")
    except Exception as e:
        print((f"Error writing to log file: {e}"))

def monitor_system():
    """Monitor and expose metrics while handling alerts."""
    while True:
        # Get CPU, memory usage, disk usage
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage(DISK_PATH).percent

        # Update Prometheus metrics
        cpu_usage_gauge.set(cpu_usage)
        memory_usage_gauge.set(memory_usage)
        disk_usage_gauge.set(disk_usage)

        if cpu_usage > CPU_THRESHOLD:
            log_event(f"High CPU Usage: {cpu_usage}%")
            send_email("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%")

        if memory_usage > MEMORY_THRESHOLD:
            log_event(f"High Memory Usage: {memory_usage}%")
            send_email("High Memory Usage Alert", f"Memory usage is at {memory_usage}%")

        if disk_usage > DISK_THRESHOLD:
            message = f"High Disk Usage on {DISK_PATH}: {disk_usage}%"
            log_event(message)
            send_email("High Disk Usage Alert", message)

        print(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%")

        time.sleep(5) 

if __name__ == "__main__":
    start_http_server(8000)
    print("Prometheus metrics availabe at http://localhost:8000/metrics")    
    monitor_system()