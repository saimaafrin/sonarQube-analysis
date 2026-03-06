
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
    
    while (time.time() - start_time) < duration:
        try:
            # Get CPU usage based on the operating system
            if platform.system().lower() == "windows":
                result = subprocess.run(["wmic", "cpu", "get", "LoadPercentage"], capture_output=True, text=True)
                cpu_usage = int(result.stdout.split('\n')[1].strip())
            else:
                result = subprocess.run(["top", "-bn1", "|", "grep", "Cpu(s)", "|", "sed", "'s/.*, *\([0-9.]*\)%* id.*/\1/'", "|", "awk", "{print 100 - $1}"], shell=True, capture_output=True, text=True)
                cpu_usage = float(result.stdout.strip())
            
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            cpu_usage_data.append({"timestamp": current_time, "cpu_usage": cpu_usage})
            
            time.sleep(interval)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    try:
        with open(LOGFILE_PATH, 'w') as log_file:
            json.dump(cpu_usage_data, log_file, indent=4)
        return LOGFILE_PATH
    except IOError as e:
        print(f"IOError occurred: {e}")
        return None