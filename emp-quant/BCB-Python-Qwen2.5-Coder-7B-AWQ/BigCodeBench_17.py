import subprocess
import psutil
import time
def task_func(process_name: str) -> str:
    # Check if the process is running
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            # Process is found, restart it
            try:
                proc.terminate()
                time.sleep(1)  # Wait for the process to terminate
                subprocess.Popen(process_name)
                return f"Process found. Restarting {process_name}."
            except Exception as e:
                return f"Error restarting {process_name}: {str(e)}"
    
    # Process not found, start it
    try:
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."
    except Exception as e:
        return f"Error starting {process_name}: {str(e)}"