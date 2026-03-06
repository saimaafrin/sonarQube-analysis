
import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None
    
    # Select a random file from the provided list
    selected_file = random.choice(file_list)
    
    # Construct the full path to the selected file
    file_path = os.path.join(directory, selected_file)
    
    # Check if the selected file exists
    if not os.path.isfile(file_path):
        return None
    
    try:
        # Run the selected file as a subprocess
        result = subprocess.run([file_path], capture_output=True, text=True)
        
        # Return the exit code of the subprocess
        return result.returncode
    except Exception as e:
        print(f"An error occurred: {e}")
        return None