
import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    # Create a temporary directory if it doesn't exist
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Copy the script to the temporary directory
    temp_script_path = os.path.join(temp_dir, 'temp_script.py')
    shutil.copy(script_path, temp_script_path)

    try:
        # Execute the script using subprocess
        result = subprocess.run(['python', temp_script_path], capture_output=True, text=True)
        
        # Check if the script executed successfully
        if result.returncode == 0:
            return "Script executed successfully!"
        else:
            return f"Script execution failed! Error: {result.stderr}"
    except Exception as e:
        return f"An error occurred: {e}"