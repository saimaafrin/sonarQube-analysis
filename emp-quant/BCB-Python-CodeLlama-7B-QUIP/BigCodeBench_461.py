
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise ValueError("Script path does not exist")

    # Execute the script in a subprocess
    process = subprocess.Popen(script_path)

    # Monitor the process for CPU and memory usage
    start_time = time.time()
    cpu_usage = 0
    memory_usage = 0
    while time.time() - start_time < timeout:
        time.sleep(0.1)
        cpu_usage = psutil.cpu_percent(process)
        memory_usage = psutil.virtual_memory()[process]

    # Ensure the subprocess is terminated
    process.terminate()

    # Return the metrics
    return {
        "CPU Usage": cpu_usage,
        "Memory Usage": memory_usage
    }