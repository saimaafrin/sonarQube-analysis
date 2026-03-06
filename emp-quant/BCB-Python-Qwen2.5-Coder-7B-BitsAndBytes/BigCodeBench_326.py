
import subprocess
import os
import sys
import glob

def task_func(directory_path):
    results = []
    
    # Find all .bat files in the given directory
    bat_files = glob.glob(os.path.join(directory_path, '*.bat'))
    
    for bat_file in bat_files:
        try:
            # Run the .bat file
            result = subprocess.run([bat_file], capture_output=True, text=True, check=False)
            
            # Append the file name and exit code to the results list
            results.append((os.path.basename(bat_file), result.returncode))
        except Exception as e:
            # If an error occurs, append the file name and None as the exit code
            results.append((os.path.basename(bat_file), None))
    
    return results

    directory_path = sys.argv[1]
    results = task_func(directory_path)
    
    for file_name, exit_code in results:
        print(f"{file_name}: {exit_code}")