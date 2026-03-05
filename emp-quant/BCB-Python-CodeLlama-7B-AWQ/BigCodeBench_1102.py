import subprocess
import shlex
from datetime import datetime
def task_func(script_path: str) -> dict:
    """
    Run an R script and return the start time, end time, decoded stdout, and decoded stderr as a dictionary.
    """
    start_time = datetime.now()
    process = subprocess.Popen(shlex.split(f"Rscript {script_path}"), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = datetime.now()
    return {
        "start_time": start_time,
        "end_time": end_time,
        "stdout": stdout.decode("utf-8"),
        "stderr": stderr.decode("utf-8"),
    }