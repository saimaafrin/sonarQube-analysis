import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"
def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be positive")

    # Get the current CPU usage percentage
    if platform.system() == "Windows":
        # Windows
        cmd = "wmic cpu get loadpercentage /value"
        output = subprocess.check_output(cmd, shell=True)
        cpu_usage = float(output.decode("utf-8").split("\n")[1].split("=")[1])
    else:
        # Unix/Linux
        cmd = "cat /proc/stat | grep 'cpu ' | awk '{print $2}'"
        output = subprocess.check_output(cmd, shell=True)
        cpu_usage = float(output.decode("utf-8").split("\n")[0])

    # Record the CPU usage percentage at regular intervals
    with open(LOGFILE_PATH, "a") as f:
        f.write(json.dumps({"timestamp": time.time(), "cpu_usage": cpu_usage}) + "\n")

    # Sleep for the specified interval
    time.sleep(interval)

    # Repeat until the specified duration is reached
    while time.time() < duration:
        task_func(interval, duration)

    return LOGFILE_PATH