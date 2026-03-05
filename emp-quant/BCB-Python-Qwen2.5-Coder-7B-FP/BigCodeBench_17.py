import subprocess
import psutil
import time
def task_func(process_name: str) -> str:
    # Check if the process is running
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            # Process is found, terminate it
            proc.kill()
            time.sleep(1)  # Wait for the process to terminate
            # Restart the process
            subprocess.Popen(process_name)
            return f"Process found. Restarting {process_name}."
    
    # Process is not found, start it
    subprocess.Popen(process_name)
    return f"Process not found. Starting {process_name}."