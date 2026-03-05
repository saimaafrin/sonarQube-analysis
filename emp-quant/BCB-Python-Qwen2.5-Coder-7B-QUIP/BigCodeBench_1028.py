
import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be greater than zero")

    def get_cpu_usage():
        if platform.system() == 'Windows':
            return subprocess.check_output("wmic cpu get loadpercentage").decode().strip()
        else:
            return subprocess.check_output("mpstat -P ALL 1 1 | tail -n 1").decode().strip()

    def log_cpu_usage():
        with open(LOGFILE_PATH, 'a') as f:
            f.write(f"{time.time()}: {get_cpu_usage()}\n")

    start_time = time.time()
    while time.time() - start_time < duration:
        log_cpu_usage()
        time.sleep(interval)

    return LOGFILE_PATH