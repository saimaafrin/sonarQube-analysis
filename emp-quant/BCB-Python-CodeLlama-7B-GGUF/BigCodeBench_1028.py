
import subprocess
import time
import json
import platform

LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be greater than 0")

    if platform.system() == "Windows":
        cmd = "wmic path Win32_Processor get LoadPercentage"
    else:
        cmd = "top -bn1 | grep '^%Cpu' | awk '{print $2}'"

    with open(LOGFILE_PATH, "w") as logfile:
        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                output = subprocess.check_output(cmd, shell=True)
                logfile.write(json.dumps({"timestamp": time.time(), "cpu_usage": float(output.decode().strip())}) + "\n")
            except subprocess.CalledProcessError:
                logfile.write(json.dumps({"timestamp": time.time(), "cpu_usage": None}) + "\n")
            time.sleep(interval)

    return LOGFILE_PATH