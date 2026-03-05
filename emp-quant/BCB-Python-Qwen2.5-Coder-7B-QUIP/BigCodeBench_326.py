
import subprocess
import os
import glob

def task_func(directory_path):
    # Initialize an empty list to store the results
    results = []
    
    # Find all .bat files in the given directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))
    
    # Iterate over each .bat file
    for bat_file in bat_files:
        # Extract the file name
        file_name = os.path.basename(bat_file)
        
        # Execute the .bat file
        try:
            # Run the subprocess and capture the exit code
            result = subprocess.run(bat_file, capture_output=True, text=True, check=True)
            exit_code = result.returncode
        except subprocess.CalledProcessError as e:
            exit_code = e.returncode
        
        # Append the file name and exit code to the results list
        results.append((file_name, exit_code))
    
    # Return the list of tuples
    return results