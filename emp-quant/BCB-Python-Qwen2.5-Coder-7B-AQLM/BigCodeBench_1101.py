
import subprocess
import os
import glob
import time

def task_func(test_dir):
    script_times = {}
    # Get all Python files in the directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    for script in python_files:
        start_time = time.time()
        # Run the script using subprocess
        result = subprocess.run(['python', script], capture_output=True, text=True)
        end_time = time.time()
        
        # Check if the script executed successfully
        if result.returncode == 0:
            execution_time = end_time - start_time
            script_times[os.path.basename(script)] = execution_time
        else:
            print(f"Error executing {script}: {result.stderr}")
    
    return script_times