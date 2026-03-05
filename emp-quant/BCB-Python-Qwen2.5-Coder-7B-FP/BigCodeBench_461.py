import subprocess
import psutil
import time
import os
def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script at {script_path} does not exist.")
    
    # Start the subprocess
    process = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Initialize CPU and memory usage
    cpu_usage = 0.0
    memory_usage = 0
    
    # Start a timer
    start_time = time.time()
    
    while True:
        # Check if the process has finished
        if process.poll() is not None:
            break
        
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            process.terminate()
            raise TimeoutError(f"The script at {script_path} exceeded the timeout of {timeout} seconds.")
        
        # Get the process object
        try:
            proc = psutil.Process(process.pid)
        except psutil.NoSuchProcess:
            process.terminate()
            raise Exception(f"The process for the script at {script_path} was not found.")
        
        # Update CPU and memory usage
        cpu_usage += proc.cpu_percent(interval=1)
        memory_usage += proc.memory_info().rss
        
        # Sleep for a short period to avoid high CPU usage
        time.sleep(0.1)
    
    # Wait for the process to finish
    process.wait()
    
    # Return the CPU and memory usage
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }