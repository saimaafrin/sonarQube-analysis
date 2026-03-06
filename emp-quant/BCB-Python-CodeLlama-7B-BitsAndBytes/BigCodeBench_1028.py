
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
        cmd = "wmic cpu get loadpercentage"
    else:
        cmd = "cat /proc/cpuinfo | grep 'cpu MHz'"
    output = subprocess.check_output(cmd, shell=True)
    cpu_usage = float(output.split()[0])

    # Open the log file and write the CPU usage data
    with open(LOGFILE_PATH, "w") as log_file:
        log_file.write("[")
        for i in range(duration // interval):
            log_file.write(f"{{'timestamp': {time.time()}, 'cpu_usage': {cpu_usage}}}\n")
            time.sleep(interval)
        log_file.write("]")

    return LOGFILE_PATH