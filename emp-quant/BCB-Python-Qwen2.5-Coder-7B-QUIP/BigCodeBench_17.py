
import subprocess
import psutil
import time

def task_func(process_name: str) -> str:
    # Check if the process is running
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            # Process is running, restart it
            subprocess.call(['taskkill', '/F', '/IM', process_name])
            time.sleep(1)  # Wait for the process to terminate
            subprocess.call([process_name])
            return f"Process found. Restarting {process_name}."
    
    # Process not found, start it
    subprocess.call([process_name])
    return f"Process not found. Starting {process_name}."