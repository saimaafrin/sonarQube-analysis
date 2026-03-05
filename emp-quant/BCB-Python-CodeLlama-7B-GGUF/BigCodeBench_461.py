
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    """
    Executes a given bash script and returns the CPU and memory usage of the script's process.

    Args:
        script_path (str): The path to the bash script to execute.
        timeout (int, optional): The maximum time to wait for the script to complete, in seconds. Defaults to 10.

    Returns:
        dict: A dictionary containing:
            'CPU Usage': The accumulated CPU usage in percentage.
            'Memory Usage': The accumulated memory usage in bytes.
    """
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script file not found: {script_path}")

    # Start the subprocess
    process = subprocess.Popen(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Create a psutil.Process object for the subprocess
    ps_process = psutil.Process(process.pid)

    # Start monitoring the process
    start_time = time.time()
    cpu_usage = 0
    memory_usage = 0
    while process.poll() is None and time.time() - start_time < timeout:
        # Get the CPU and memory usage of the process
        cpu_usage += ps_process.cpu_percent(interval=1)
        memory_usage += ps_process.memory_info().rss

        # Sleep for 1 second
        time.sleep(1)

    # Get the final CPU and memory usage of the process
    cpu_usage += ps_process.cpu_percent(interval=1)
    memory_usage += ps_process.memory_info().rss

    # Terminate the subprocess if it runs beyond the timeout
    if time.time() - start_time >= timeout:
        process.terminate()

    # Return the CPU and memory usage
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }