import subprocess
import shlex
from datetime import datetime
def task_func(script_path: str) -> dict:
    # Start time
    start_time = datetime.now()
    
    # Run the R script
    process = subprocess.Popen(['Rscript', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Capture stdout and stderr
    stdout, stderr = process.communicate()
    
    # End time
    end_time = datetime.now()
    
    # Return the results as a dictionary
    return {
        'start_time': start_time,
        'end_time': end_time,
        'stdout': stdout,
        'stderr': stderr
    }