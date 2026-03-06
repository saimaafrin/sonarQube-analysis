
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise ValueError(f"Script path {script_path} does not exist")

    # Execute the script in a subprocess
    process = subprocess.Popen(script_path, shell=True)

    # Monitor the process for CPU and memory usage
    cpu_usage = 0
    memory_usage = 0
    start_time = time.time()
    while process.poll() is None:
        cpu_usage += psutil.cpu_percent(interval=1)
        memory_usage += psutil.virtual_memory().rss
        if time.time() - start_time > timeout:
            process.terminate()
            raise TimeoutError(f"Script {script_path} timed out after {timeout} seconds")

    # Return the CPU and memory usage
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }