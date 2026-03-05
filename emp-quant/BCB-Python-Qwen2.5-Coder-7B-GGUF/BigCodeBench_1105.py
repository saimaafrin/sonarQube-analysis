
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    start_time = time.time()
    # Execute the R script
    subprocess.run(['Rscript', r_script_path], check=True)
    
    # Wait for the output file to be generated
    while time.time() - start_time < duration:
        if glob.glob(output_path):
            return True, 'File generated successfully within the specified duration.'
        time.sleep(1)
    
    return False, 'File not generated within the specified duration.'