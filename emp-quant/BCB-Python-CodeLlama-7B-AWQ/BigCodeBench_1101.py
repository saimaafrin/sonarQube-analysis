import subprocess
import os
import glob
import time
def task_func(test_dir):
    """
    Runs all Python codes in a specific directory and returns their execution times.
    :param test_dir: The directory containing the Python codes.
    :return: A dictionary with the script names as keys and their execution times as values.
    """
    # Create a dictionary to store the execution times
    execution_times = {}

    # Get a list of all Python files in the directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))

    # Iterate over the Python files
    for python_file in python_files:
        # Get the script name
        script_name = os.path.basename(python_file)

        # Run the script and measure its execution time
        start_time = time.time()
        subprocess.run(['python', python_file], check=True)
        end_time = time.time()

        # Add the execution time to the dictionary
        execution_times[script_name] = end_time - start_time

    # Return the dictionary of execution times
    return execution_times
test_dir = 'path/to/test/directory'