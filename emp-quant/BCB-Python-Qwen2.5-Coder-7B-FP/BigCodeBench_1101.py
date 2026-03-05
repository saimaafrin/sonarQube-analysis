import subprocess
import os
import glob
import time
def task_func(test_dir):
    # Dictionary to store script names and their execution times
    execution_times = {}
    
    # Get a list of all Python files in the specified directory
    python_files = glob.glob(os.path.join(test_dir, '*.py'))
    
    # Iterate over each Python file
    for file in python_files:
        # Get the script name without the path and extension
        script_name = os.path.basename(file)
        
        # Start the timer
        start_time = time.time()
        
        # Run the Python script using subprocess
        result = subprocess.run(['python', file], capture_output=True, text=True)
        
        # Stop the timer
        end_time = time.time()
        
        # Calculate the execution time
        execution_time = end_time - start_time
        
        # Store the execution time in the dictionary
        execution_times[script_name] = execution_time
    
    # Return the dictionary with script names and their execution times
    return execution_times