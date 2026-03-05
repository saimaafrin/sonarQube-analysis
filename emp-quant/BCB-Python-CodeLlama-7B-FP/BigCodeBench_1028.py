import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"
def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be positive")

    if platform.system() == "Windows":
        # Windows command to get CPU usage
        cmd = "wmic cpu get loadpercentage"
    else:
        # Unix/Linux command to get CPU usage
        cmd = "top -b -n 1 | awk '{print $9}'"

    # Open log file for writing
    with open(LOGFILE_PATH, "w") as logfile:
        # Write header to log file
        logfile.write("timestamp,cpu_usage\n")

        # Loop for specified duration
        start_time = time.time()
        while time.time() - start_time < duration:
            # Run command to get CPU usage
            output = subprocess.check_output(cmd, shell=True)

            # Parse output to get CPU usage percentage
            cpu_usage = float(output.decode("utf-8").strip())

            # Write data to log file
            logfile.write(f"{time.time()},{cpu_usage}\n")

            # Sleep for specified interval
            time.sleep(interval)

    # Return path to log file
    return LOGFILE_PATH