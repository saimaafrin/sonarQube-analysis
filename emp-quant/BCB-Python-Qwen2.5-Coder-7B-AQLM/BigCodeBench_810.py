
import re
import os
import subprocess

def task_func(dir_path, exe_pattern, execute_files=True):
    results = []
    # Compile the regular expression pattern
    pattern = re.compile(exe_pattern)
    
    # Walk through the directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file matches the pattern
            if pattern.match(file):
                file_path = os.path.join(root, file)
                if execute_files:
                    # Execute the file and capture the output
                    try:
                        output = subprocess.check_output([file_path], stderr=subprocess.STDOUT, universal_newlines=True)
                        results.append(output)
                    except subprocess.CalledProcessError as e:
                        results.append(e.output)
                else:
                    # Append the file path to the results
                    results.append(file_path)
    
    return results