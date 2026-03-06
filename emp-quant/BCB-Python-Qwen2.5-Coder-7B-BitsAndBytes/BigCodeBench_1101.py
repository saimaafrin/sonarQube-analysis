
import subprocess
import os
import glob
import time

def task_func(test_dir):
    # Dictionary to store the execution times of each script
    execution_times = {}
    
    # Get a list of all Python files in the specified directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    for file_path in python_files:
        # Extract the script name without the path and extension
        script_name = os.path.basename(file_path).split('.')[0]
        
        start_time = time.time()
        
        try:
            # Run the Python script using subprocess
            result = subprocess.run(['python', file_path], check=True, capture_output=True, text=True)
            
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Store the execution time in the dictionary
            execution_times[script_name] = execution_time
        
        except subprocess.CalledProcessError as e:
            print(f"Error running {script_name}: {e}")
            execution_times[script_name] = None
    
    return execution_times