
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    start_time = time.time()
    subprocess.call(['Rscript', r_script_path])
    end_time = time.time()
    elapsed_time = end_time - start_time
    if glob.glob(output_path):
        if elapsed_time <= duration:
            return True, 'File generated successfully within the specified duration.'
        else:
            return False, 'File not generated within the specified duration.'
    else:
        return False, 'File not generated within the specified duration.'