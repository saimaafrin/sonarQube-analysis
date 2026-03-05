import subprocess
import os
import glob
import time
def task_func(test_dir):
    """
    Run all Python codes in a specific directory and return their execution times.
    """
    # Create a dictionary to store the script names and their execution times
    script_times = {}

    # Get all Python files in the test directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))

    # Iterate over the Python files and run each one
    for python_file in python_files:
        # Get the script name from the file path
        script_name = os.path.basename(python_file)

        # Run the script and get the execution time
        start_time = time.time()
        subprocess.run(['python', python_file], check=True)
        end_time = time.time()

        # Add the script name and execution time to the dictionary
        script_times[script_name] = end_time - start_time

    # Return the dictionary of script names and execution times
    return script_times
test_dir = 'path/to/test/directory'