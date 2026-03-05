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

    # Iterate over all .bat files in the directory
    for file in glob.glob(os.path.join(directory_path, '*.bat')):
        # Run the .bat file and get its exit code
        try:
            process = subprocess.run(file, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            exit_code = process.returncode
        except subprocess.CalledProcessError:
            exit_code = None

        # Add the file name and exit code to the results list
        results.append((file, exit_code))

    # Return the results
    return results
directory_path = 'C:\\Users\\User\\Documents'