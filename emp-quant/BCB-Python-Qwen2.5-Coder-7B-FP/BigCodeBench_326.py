import subprocess
import os
import sys
import glob
def task_func(directory_path):
    result = []
    # Use glob to find all .bat files in the given directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))
    for bat_file in bat_files:
        try:
            # Execute the .bat file and capture the exit code
            exit_code = subprocess.call(bat_file, shell=True)
            result.append((bat_file, exit_code))
        except Exception as e:
            # If an error occurs, append the file name and None as the exit code
            result.append((bat_file, None))
    return result