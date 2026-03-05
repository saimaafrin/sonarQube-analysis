import subprocess
import shlex
from datetime import datetime
def task_func(script_path: str) -> dict:
    # Start time
    start_time = datetime.now()
    
    # Run the R script
    result = subprocess.run(['Rscript', script_path], capture_output=True, text=True)
    
    # End time
    end_time = datetime.now()
    
    # Decode stdout and stderr
    stdout = result.stdout
    stderr = result.stderr
    
    # Create the result dictionary
    result_dict = {
        'start_time': start_time,
        'end_time': end_time,
        'stdout': stdout,
        'stderr': stderr
    }
    
    return result_dict