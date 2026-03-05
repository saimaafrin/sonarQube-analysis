
import subprocess
import os
import glob
import time

def task_func(test_dir):
    # Create a list of all Python files in the test directory
    python_files = glob.glob(test_dir + "/*.py")

    # Create a dictionary to store the execution times
    execution_times = {}

    # Loop through each Python file and execute it
    for file in python_files:
        execution_times[file] = time.time()
        subprocess.run(["python", file])

    # Return the execution times
    return execution_times