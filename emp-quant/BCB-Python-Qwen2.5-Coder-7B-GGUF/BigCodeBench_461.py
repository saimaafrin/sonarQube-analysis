
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script at {script_path} does not exist.")
    
    process = None
    try:
        process = subprocess.Popen(script_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        start_time = time.time()
        cpu_usage = 0.0
        memory_usage = 0
        
        while process.poll() is None and time.time() - start_time < timeout:
            time.sleep(1)
            try:
                proc = psutil.Process(process.pid)
                cpu_usage += proc.cpu_percent(interval=1)
                memory_usage += proc.memory_info().rss
            except psutil.NoSuchProcess:
                break
        
        if process.poll() is None:
            process.terminate()
            process.wait()
        
        return {
            'CPU Usage': cpu_usage,
            'Memory Usage': memory_usage
        }
    except Exception as e:
        if process:
            process.terminate()
            process.wait()
        raise e