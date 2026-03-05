
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
            print(f"Script not found: {script_path}")
            continue
        start_time = datetime.now()
        timestamps.append(start_time)
        print(f"Executing {script_path} at {start_time}")
        subprocess.run([script_path], check=True)
        time.sleep(delay)
    
    return timestamps