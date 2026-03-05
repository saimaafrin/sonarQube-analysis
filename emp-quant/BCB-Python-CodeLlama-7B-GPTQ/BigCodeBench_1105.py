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
    # Execute the R script
    subprocess.run(r_script_path, shell=True)

    # Wait for the output file to be generated
    start_time = time.time()
    while not os.path.exists(output_path):
        time.sleep(1)
        if time.time() - start_time > duration:
            return False, "File not generated within the specified duration."

    # Check if the output file is generated successfully
    if os.path.exists(output_path):
        return True, "File generated successfully within the specified duration."
    else:
        return False, "File not generated within the specified duration."
r_script_path = "path/to/r_script.R"
output_path = "path/to/output_file.txt"
duration = 10