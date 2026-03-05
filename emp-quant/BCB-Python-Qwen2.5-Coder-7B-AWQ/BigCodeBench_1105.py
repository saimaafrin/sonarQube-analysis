import subprocess
import os
import time
import glob
def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    # Start the R script execution
    start_time = time.time()
    process = subprocess.Popen(['Rscript', r_script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Wait for the process to finish or until the duration is exceeded
    while process.poll() is None and time.time() - start_time < duration:
        time.sleep(1)
    
    # Check if the process is still running after the duration
    if process.poll() is None:
        process.terminate()
        return False, 'File not generated within the specified duration.'
    
    # Check if the output file exists
    if os.path.exists(output_path):
        return True, 'File generated successfully within the specified duration.'
    else:
        return False, 'File not generated within the specified duration.'
r_script_path = 'path_to_your_r_script.R'
output_path = 'path_to_your_output_file.txt'
duration = 10