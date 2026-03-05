
import subprocess
import os
import time
import glob

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    """
    Executes an R script and verifies if the output file is generated within a given duration.

    Parameters:
    r_script_path (str): Path to the R script to be executed.
    output_path (str): Path to the output file to be generated.
    duration (int): Duration in seconds within which the output file should be generated.

    Returns:
    tuple containing:
    bool: True if the output file is generated within the specified duration, False otherwise.
    str: A message indicating whether the file was generated successfully or not. If the generation is successful, the message will be 'File generated successfully within the specified duration.'; otherwise, it will be 'File not generated within the specified duration.'
    """
    # Start the R script
    subprocess.run(["Rscript", r_script_path])

    # Wait for the output file to be generated
    start_time = time.time()
    while not os.path.exists(output_path):
        if time.time() - start_time > duration:
            return False, "File not generated within the specified duration."
        time.sleep(1)

    # Check if the output file is generated
    if os.path.exists(output_path):
        return True, "File generated successfully within the specified duration."
    else:
        return False, "File not generated within the specified duration."