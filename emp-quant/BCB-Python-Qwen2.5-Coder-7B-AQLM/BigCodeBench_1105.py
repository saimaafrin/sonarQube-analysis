
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    # Start the R script execution
    process = subprocess.Popen(['Rscript', r_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Start the timer
    start_time = time.time()
    
    # Wait for the output file to be generated or the duration to elapse
    while True:
        if time.time() - start_time > duration:
            process.terminate()
            return False, 'File not generated within the specified duration.'
        
        if glob.glob(output_path):
            return True, 'File generated successfully within the specified duration.'
        
        time.sleep(1)