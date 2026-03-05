
import subprocess
import psutil
import time

def task_func(process_name: str) -> str:
    process = psutil.Process(process_name)
    if not process.is_running():
        subprocess.Popen(process_name)
        return f"Process not found. Starting {process_name}."
    else:
        process.terminate()
        time.sleep(1)
        subprocess.Popen(process_name)
        return f"Process found. Restarting {process_name}."