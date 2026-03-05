import subprocess
import os
import sys
import glob
def task_func(directory_path):
    """
    Find and run all .bat files in a given directory, returning their file names and exit codes.
    """
    # Create a list to store the results
    results = []

    # Get a list of all .bat files in the directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))

    # Iterate over the list of .bat files
    for bat_file in bat_files:
        # Run the .bat file and get the exit code
        try:
            process = subprocess.run(bat_file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            exit_code = process.returncode
        except Exception as e:
            # If there was an error running the .bat file, set the exit code to None
            exit_code = None

        # Add the file name and exit code to the results list
        results.append((os.path.basename(bat_file), exit_code))

    # Return the results list
    return results