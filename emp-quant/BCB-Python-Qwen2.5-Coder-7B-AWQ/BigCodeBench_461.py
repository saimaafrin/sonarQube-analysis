import subprocess
import psutil
import time
import os
def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script not found: {script_path}")

    # Initialize CPU and memory usage counters
    cpu_usage = 0.0
    memory_usage = 0

    # Start the subprocess
    process = subprocess.Popen(script_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Start monitoring the process
    start_time = time.time()
    while process.poll() is None and time.time() - start_time < timeout:
        # Get the process object
        proc = psutil.Process(process.pid)
        
        # Get CPU and memory usage
        cpu_usage += proc.cpu_percent(interval=1)
        memory_usage += proc.memory_info().rss

    # Ensure the subprocess is terminated if it runs beyond the timeout
    if process.poll() is None:
        process.terminate()
        process.wait()

    # Return the CPU and memory usage
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }