
import subprocess
import os
import sys
import glob

def task_func(directory_path):
    # Get a list of all .bat files in the directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))

    # Initialize a list to store the results
    results = []

    # Iterate over the .bat files and run them
    for bat_file in bat_files:
        # Run the .bat file and get the exit code
        try:
            process = subprocess.run(bat_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            exit_code = process.returncode
        except Exception as e:
            exit_code = None

        # Add the file name and exit code to the results list
        results.append((os.path.basename(bat_file), exit_code))

    # Return the results
    return results