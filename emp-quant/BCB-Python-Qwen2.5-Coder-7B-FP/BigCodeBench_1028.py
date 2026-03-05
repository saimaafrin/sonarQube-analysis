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
            result = subprocess.run(["wmic", "cpu", "get", "LoadPercentage"], capture_output=True, text=True)
            cpu_usage = int(result.stdout.split('\n')[1].strip())
        else:
            result = subprocess.run(["top", "-bn1", "|", "grep", "Cpu(s)"], shell=True, capture_output=True, text=True)
            cpu_usage = int(result.stdout.split()[2].strip('%'))
        
        cpu_usage_data.append({"timestamp": timestamp, "cpu_usage": cpu_usage})
        time.sleep(interval)
    
    try:
        with open(LOGFILE_PATH, 'w') as file:
            json.dump(cpu_usage_data, file, indent=4)
        return LOGFILE_PATH
    except IOError:
        return None