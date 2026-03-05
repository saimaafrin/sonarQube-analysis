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
    cpu_usage = 0
    memory_usage = 0
    
    # Start a timer
    start_time = time.time()
    
    # Monitor the process
    while process.poll() is None:
        # Check if the process has become a zombie
        if process.status() == psutil.STATUS_ZOMBIE:
            process.terminate()
            raise Exception("The process has become a zombie.")
        
        # Get the process object
        proc = psutil.Process(process.pid)
        
        # Update CPU and memory usage
        cpu_usage += proc.cpu_percent(interval=1)
        memory_usage += proc.memory_info().rss
        
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            process.terminate()
            raise Exception("The script execution exceeded the timeout.")
        
        # Sleep for a short interval to avoid high CPU usage
        time.sleep(0.1)
    
    # Get the final CPU and memory usage
    cpu_usage += proc.cpu_percent(interval=1)
    memory_usage += proc.memory_info().rss
    
    # Return the results as a dictionary
    return {
        'CPU Usage': cpu_usage,
        'Memory Usage': memory_usage
    }