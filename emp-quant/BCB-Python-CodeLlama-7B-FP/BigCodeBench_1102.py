import subprocess
import shlex
from datetime import datetime
def task_func(script_path: str) -> dict:
    """
    Run an R script and return the start time, end time, decoded stdout, and decoded stderr as a dictionary.
    """
    # Start time
    start_time = datetime.now()

    # Run the R script
    process = subprocess.run(
        ["Rscript", script_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )

    # End time
    end_time = datetime.now()

    # Decode the stdout and stderr
    stdout = process.stdout.decode("utf-8")
    stderr = process.stderr.decode("utf-8")

    # Create the dictionary
    result = {
        "start_time": start_time,
        "end_time": end_time,
        "stdout": stdout,
        "stderr": stderr,
    }

    return result
script_path = "script.R"