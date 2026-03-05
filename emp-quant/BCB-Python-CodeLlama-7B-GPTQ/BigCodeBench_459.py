import subprocess
import os
import time
from datetime import datetime
def task_func(script_dir, scripts, delay):
    """
    Execute a list of bash scripts with a specified delay between each script.
    The function should raise the exception for:
        ValueError: If the delay is negative or no scripts are provided.
    The function should output with:
        list: A list of timestamps indicating the start time of each script execution.
    """
    if delay < 0 or not scripts:
        raise ValueError("Invalid input")

    start_time = datetime.now()
    script_times = []
    for script in scripts:
        script_times.append(start_time)
        subprocess.run(f"{script_dir}/{script}", shell=True)
        time.sleep(delay)
        start_time += datetime.timedelta(seconds=delay)

    return script_times