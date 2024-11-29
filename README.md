# System-Health-Monitor
The System Health Monitor is a Python-based utility designed to help track and maintain the performance of your system. This tool continuously monitors critical system resources such as CPU usage, memory usage, and disk space, ensuring that your system runs smoothly without any unexpected performance drops.

The script uses the power of Python’s psutil library to fetch real-time system metrics and logs the results into a well-organized log file (system_health.log). Whenever resource usage exceeds predefined thresholds, it provides instant alerts to the console while also recording warnings in the log file.

### Key Features
Real-Time System Monitoring: Continuously tracks critical system metrics, including:

CPU Usage – Ensures your processor isn't overwhelmed.
Memory Usage – Keeps an eye on available RAM to prevent slowdowns.
Disk Usage – Alerts you when disk space is running low.
Detailed Logging: Automatically logs system health data to a comprehensive system_health.log file for future reference.

Instant Alerts: Sends immediate alerts to the console if any of the system metrics exceed the set thresholds, ensuring you stay informed of any potential issues.

Smooth Operation: Designed for continuous operation with a exit, it stops safely upon user interruption, providing clear feedback with a message when terminated.

### Usage
To run the System Health Monitor script, follow these steps:

**Install Required Dependencies**
Make sure you have Python installed on your system. You will also need to install the psutil library, which is used to gather system statistics.

You can install the required dependency using pip:
```bash
pip install psutil
```
**Running the Script**
After installing the required dependencies, you can run the script directly from the command line:

```bash
python system_health_monitor.py
```
**Monitoring the System**
The script will start monitoring your system's health, checking the CPU usage, memory usage, and disk usage in real-time.
If any metric exceeds the defined thresholds (80% by default), an alert will be displayed in the console, and a warning will be logged in the system_health.log file.
If everything is normal, the script will log the system health data with usage percentages for CPU, memory, and disk.

**Stopping the Script**
You can stop the script at any time by pressing Ctrl+C. The script will exit gracefully with a message informing you that the monitoring was stopped by the user.
Monitoring stopped by user. Exiting the program...

**View Logs**
All system health data, including any alerts, are logged to the system_health.log file. You can open this file to review the log entries or troubleshoot any issues.
