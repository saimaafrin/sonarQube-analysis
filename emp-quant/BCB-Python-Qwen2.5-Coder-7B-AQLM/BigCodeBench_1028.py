
import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be greater than zero.")
    
    cpu_usage_data = []
    start_time = time.time()
    
    while time.time() - start_time < duration:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if platform.system() == "Windows":
            cpu_usage = subprocess.check_output(["wmic", "cpu", "get", "LoadPercentage"], shell=True).decode().split('\n')[1].strip()
        else:
            cpu_usage = subprocess.check_output(["top", "-bn1", "|", "grep", "Cpu(s)", "|", "awk", "{print $2 + $4}"], shell=True).decode().split('\n')[0].strip()
        
        cpu_usage_data.append({"timestamp": timestamp, "cpu_usage": int(cpu_usage)})
        time.sleep(interval)
    
    try:
        with open(LOGFILE_PATH, 'w') as log_file:
            json.dump(cpu_usage_data, log_file, indent=4)
        return LOGFILE_PATH
    except IOError:
        return None