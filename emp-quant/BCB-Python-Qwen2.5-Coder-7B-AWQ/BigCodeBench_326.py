import subprocess
import os
import sys
import glob
def task_func(directory_path):
    """
    Find and run all .bat files in a given directory, returning their file names and exit codes.
    
    :param directory_path: str - The path to the directory containing .bat files.
    :return: list of tuples - A list where each tuple contains the file name and its exit code.
             The exit code is None if the file could not be executed.
    """
    # Initialize an empty list to store the results
    results = []
    
    # Use glob to find all .bat files in the directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))
    
    # Iterate over each .bat file
    for bat_file in bat_files:
        try:
            # Run the .bat file using subprocess
            result = subprocess.run([bat_file], capture_output=True, text=True, check=True)
            # Append the file name and exit code to the results list
            results.append((bat_file, result.returncode))
        except subprocess.CalledProcessError as e:
            # If the file could not be executed, append the file name and None as the exit code
            results.append((bat_file, None))
        except Exception as e:
            # Handle any other exceptions and append the file name and None as the exit code
            results.append((bat_file, None))
    
    # Return the list of tuples containing file names and exit codes
    return results