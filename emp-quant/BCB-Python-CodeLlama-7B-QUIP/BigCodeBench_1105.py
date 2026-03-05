
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    """
    This function executes an R script and verifies if the output file is generated within a given duration.
    The function should output with:
        tuple containing:
            bool: True if the output file is generated within the specified duration, False otherwise.
            str: A message indicating whether the file was generated successfully or not. If the generation is successful, the message will be 'File generated successfully within the specified duration.'; otherwise, it will be 'File not generated within the specified duration.'
    """
    start_time = time.time()
    subprocess.run(["R", r_script_path])
    end_time = time.time()
    duration_time = end_time - start_time
    if duration_time < duration:
        return (False, "File not generated within the specified duration.")
    else:
        return (True, "File generated successfully within the specified duration.")
    output_file = glob.glob(output_path + "/*.csv")
    if len(output_file) == 0:
        return (False, "File not generated within the specified duration.")
    else:
        return (True, "File generated successfully within the specified duration.")