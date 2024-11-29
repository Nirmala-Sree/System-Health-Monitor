import psutil
import logging
import time

# logging to store system health information
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def monitor_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Checking CPU usage
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
        print(f"ALERT: CPU usage is {cpu_usage}%")
    else:
        logging.info(f"CPU usage: {cpu_usage}%")

    # Checking Memory usage
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_usage}%")
        print(f"ALERT: Memory usage is {memory_usage}%")
    else:
        logging.info(f"Memory usage: {memory_usage}%")

    # Checking Disk usage
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"Low disk space: {disk_usage}% used")
        print(f"ALERT: Disk usage is {disk_usage}%")
    else:
        logging.info(f"Disk usage: {disk_usage}%")

    # Logging overall system health
    logging.info(f"System Health - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%")

# Continuous monitoring loop with exit on interruption
if __name__ == "__main__":
    try:
        while True:
            monitor_system_health()  # Check system health
            time.sleep(10)  # Wait for 10 seconds before checking again
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user. Exiting the program...")  
