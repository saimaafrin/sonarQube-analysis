
import subprocess
import time
import json
import platform
LOGFILE_PATH = "logfile.log"

def task_func(interval, duration):
    if interval <= 0 or duration <= 0:
        raise ValueError("Interval and duration must be greater than zero.")
    
    try:
        with open(LOGFILE_PATH, 'w') as log_file:
            start_time = time.time()
            while time.time() - start_time < duration:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if platform.system() == "Windows":
                    cpu_usage = subprocess.check_output(["wmic", "cpu", "get", "LoadPercentage"], shell=True).decode().strip().split('\n')[1].strip()
                else:
                    cpu_usage = subprocess.check_output(["top", "-bn1", "|", "grep", "Cpu(s)"], shell=True).decode().strip().split('\n')[0].split(',')[0].strip().split()[1]
                log_entry = {"timestamp": timestamp, "cpu_usage": cpu_usage}
                log_file.write(json.dumps(log_entry) + '\n')
                time.sleep(interval)
        return LOGFILE_PATH
    except IOError as e:
        print(f"IOError occurred: {e}")
        return None