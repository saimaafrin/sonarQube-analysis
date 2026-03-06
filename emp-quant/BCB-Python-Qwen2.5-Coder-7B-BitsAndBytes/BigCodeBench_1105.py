
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    start_time = time.time()
    
    # Execute the R script using subprocess
    result = subprocess.run(['Rscript', r_script_path], capture_output=True, text=True)
    
    if result.returncode != 0:
        return False, 'Error executing R script: {}'.format(result.stderr)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Check if the output file exists within the specified duration
    files = glob.glob(output_path + '*')
    if files:
        return True, 'File generated successfully within the specified duration.'
    else:
        return False, 'File not generated within the specified duration.'