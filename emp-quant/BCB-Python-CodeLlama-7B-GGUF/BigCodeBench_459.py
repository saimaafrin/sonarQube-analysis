
import subprocess
import os
import time
from datetime import datetime

def task_func(script_dir, scripts, delay):
    if delay < 0 or not scripts:
        raise ValueError("Invalid input")

    timestamps = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        subprocess.run(script_path, shell=True)
        timestamps.append(datetime.now())
        time.sleep(delay)

    return timestamps