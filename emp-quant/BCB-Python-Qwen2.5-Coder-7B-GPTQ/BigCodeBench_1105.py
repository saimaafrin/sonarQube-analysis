import subprocess
import os
import time
import glob
def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    # Start the R script execution
    start_time = time.time()
    subprocess.run(['Rscript', r_script_path], check=True)
    end_time = time.time()
    
    # Check if the output file is generated within the specified duration
    if end_time - start_time <= duration:
        # Check if the output file exists
        if glob.glob(output_path):
            return True, 'File generated successfully within the specified duration.'
        else:
            return False, 'File not generated within the specified duration.'
    else:
        return False, 'File not generated within the specified duration.'
r_script_path = 'path_to_your_r_script.R'
output_path = 'path_to_your_output_file.txt'
duration = 10