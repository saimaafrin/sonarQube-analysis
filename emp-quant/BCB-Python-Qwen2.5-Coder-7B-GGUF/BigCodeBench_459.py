
import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0:
        raise ValueError("Delay cannot be negative")
    if not scripts:
        raise ValueError("No scripts provided")
    
    timestamps = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script {script} not found in {script_dir}")
        
        start_time = datetime.now()
        timestamps.append(start_time)
        subprocess.run([script_path], shell=True)
        time.sleep(delay)
    
    return timestamps