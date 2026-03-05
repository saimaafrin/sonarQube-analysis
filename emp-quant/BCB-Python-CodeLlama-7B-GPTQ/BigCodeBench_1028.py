import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"
def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be positive integers")

    if platform.system() == "Windows":
        command = "wmic cpu get loadpercentage"
    else:
        command = "cat /proc/stat | grep 'cpu ' | awk '{print $2}'"

    with open(LOGFILE_PATH, "w") as logfile:
        start_time = time.time()
        while time.time() - start_time < duration:
            try:
                output = subprocess.check_output(command, shell=True)
                data = json.loads(output)
                logfile.write(f"{time.time()}, {data['LoadPercentage']}\n")
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
                return None
            time.sleep(interval)

    return LOGFILE_PATH