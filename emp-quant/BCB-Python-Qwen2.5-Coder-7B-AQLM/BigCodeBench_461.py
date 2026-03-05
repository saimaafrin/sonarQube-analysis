
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script path {script_path} does not exist.")
    
    cpu_usage = 0.0
    memory_usage = 0
    
    process = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    start_time = time.time()
    while process.poll() is None and time.time() - start_time < timeout:
        try:
            process_info = psutil.Process(process.pid)
            cpu_usage += process_info.cpu_percent(interval=1)
            memory_usage += process_info.memory_info().rss
        except psutil.NoSuchProcess:
            break
        except psutil.AccessDenied:
            break
        except psutil.ZombieProcess:
            break
        time.sleep(1)
    
    if process.poll() is None:
        process.terminate()
        process.wait()
    
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }