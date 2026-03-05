
import subprocess
import os
import sys
import glob

def task_func(directory_path):
    results = []
    # Use glob to find all .bat files in the given directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))
    
    for bat_file in bat_files:
        try:
            # Execute the .bat file
            result = subprocess.run([bat_file], capture_output=True, text=True, check=True)
            # Append the file name and exit code to the results list
            results.append((bat_file, result.returncode))
        except subprocess.CalledProcessError as e:
            # If the file could not be executed, append the file name and None as the exit code
            results.append((bat_file, None))
        except Exception as e:
            # Handle any other exceptions and append the file name and None as the exit code
            results.append((bat_file, None))
    
    return results