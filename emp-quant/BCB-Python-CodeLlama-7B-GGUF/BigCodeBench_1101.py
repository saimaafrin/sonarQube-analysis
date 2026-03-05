
import subprocess
import os
import glob
import time

def task_func(test_dir):
    # Create a dictionary to store the script names and their execution times
    script_times = {}

    # Get a list of all Python scripts in the test directory
    script_paths = glob.glob(os.path.join(test_dir, '*.py'))

    # Iterate over the scripts and run them
    for script_path in script_paths:
        # Get the script name
        script_name = os.path.basename(script_path)

        # Run the script and measure its execution time
        start_time = time.time()
        subprocess.run(['python', script_path])
        end_time = time.time()

        # Add the script name and execution time to the dictionary
        script_times[script_name] = end_time - start_time

    # Return the dictionary of script names and execution times
    return script_times