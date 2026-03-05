import re
import os
import subprocess
def task_func(dir_path, exe_pattern, execute_files=True):
    results = []
    # Compile the regular expression pattern for better performance
    pattern = re.compile(exe_pattern)
    
    # Walk through the directory
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            # Check if the file is executable and matches the pattern
            if os.access(os.path.join(root, file), os.X_OK) and pattern.match(file):
                if execute_files:
                    # Execute the file and capture the output
                    try:
                        output = subprocess.check_output([os.path.join(root, file)], stderr=subprocess.STDOUT)
                        results.append(output.decode('utf-8'))
                    except subprocess.CalledProcessError as e:
                        results.append(e.output.decode('utf-8'))
                else:
                    # Append the file path to the results
                    results.append(os.path.join(root, file))
    
    return results