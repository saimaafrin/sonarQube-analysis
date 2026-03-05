
import subprocess
import os
import glob
import time

def task_func(test_dir):
    script_times = {}
    # Get all Python files in the directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    for file in python_files:
        start_time = time.time()
        # Run the Python script
        result = subprocess.run(['python', file], capture_output=True, text=True)
        end_time = time.time()
        
        # Check if the script executed successfully
        if result.returncode == 0:
            script_name = os.path.basename(file)
            execution_time = end_time - start_time
            script_times[script_name] = execution_time
        else:
            print(f"Error executing {file}: {result.stderr}")
    
    return script_times