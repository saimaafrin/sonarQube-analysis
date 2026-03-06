
import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    # Run the R script and capture the output
    process = subprocess.run(shlex.split(script_path), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the start and end times of the script run
    start_time = datetime.now()
    end_time = datetime.now()

    # Decode the stdout and stderr output
    stdout = process.stdout.decode('utf-8')
    stderr = process.stderr.decode('utf-8')

    # Create a dictionary with the start and end times, stdout, and stderr
    output = {
        'start_time': start_time,
        'end_time': end_time,
        'stdout': stdout,
        'stderr': stderr
    }

    return output