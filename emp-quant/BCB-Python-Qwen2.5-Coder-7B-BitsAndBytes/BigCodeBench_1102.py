
import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    # Start time
    start_time = datetime.now()
    
    # Command to run the R script
    command = f"Rscript {shlex.quote(script_path)}"
    
    # Run the command using subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the command to complete
    stdout, stderr = process.communicate()
    
    # End time
    end_time = datetime.now()
    
    # Decode the output and error
    decoded_stdout = stdout.decode('utf-8')
    decoded_stderr = stderr.decode('utf-8')
    
    # Return the results as a dictionary
    result = {
        'start_time': start_time,
        'end_time': end_time,
        'stdout': decoded_stdout,
        'stderr': decoded_stderr
    }
    
    return result