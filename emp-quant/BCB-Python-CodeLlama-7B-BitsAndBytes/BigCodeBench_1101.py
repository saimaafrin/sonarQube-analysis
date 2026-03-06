
import subprocess
import os
import glob
import time

def task_func(test_dir):
    # Create a dictionary to store the script names and their execution times
    script_times = {}

    # Loop through all Python scripts in the test directory
    for script in glob.glob(os.path.join(test_dir, '*.py')):
        # Run the script and measure its execution time
        start_time = time.time()
        subprocess.run(script, shell=True)
        end_time = time.time()

        # Add the script name and execution time to the dictionary
        script_times[script] = end_time - start_time

    # Return the dictionary of script names and execution times
    return script_times

# Print the dictionary of script names and execution times
print(script_times)