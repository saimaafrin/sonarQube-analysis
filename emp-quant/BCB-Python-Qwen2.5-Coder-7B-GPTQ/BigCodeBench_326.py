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
            # Execute the .bat file and capture the exit code
            result = subprocess.run([bat_file], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            exit_code = result.returncode
        except subprocess.CalledProcessError as e:
            # If an error occurs, capture the exit code
            exit_code = e.returncode
        except Exception as e:
            # If any other exception occurs, set exit code to None
            exit_code = None
        
        # Append the file name and exit code to the results list
        results.append((bat_file, exit_code))
    
    return results