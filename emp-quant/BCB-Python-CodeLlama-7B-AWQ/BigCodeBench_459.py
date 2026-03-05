import subprocess
import os
import time
from datetime import datetime
def task_func(script_dir, scripts, delay):
    """
    Execute a list of bash scripts with a specified delay between each script.
    Raises ValueError if the delay is negative or no scripts are provided.
    Returns a list of timestamps indicating the start time of each script execution.
    """
    if delay < 0 or not scripts:
        raise ValueError("Invalid input")
    timestamps = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        subprocess.run(["bash", script_path])
        timestamps.append(datetime.now())
        time.sleep(delay)
    return timestamps