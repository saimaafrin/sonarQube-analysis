import subprocess
import shutil
import os
def task_func(script_path: str, temp_dir: str) -> str:
    # Create a temporary directory if it doesn't exist
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    # Copy the script to the temporary directory
    script_name = os.path.basename(script_path)
    temp_script_path = os.path.join(temp_dir, script_name)
    shutil.copy(script_path, temp_script_path)
    
    # Execute the script in the temporary directory
    try:
        result = subprocess.run(['python', temp_script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "Script executed successfully!"
    except subprocess.CalledProcessError as e:
        return f"Script execution failed! Error: {e.stderr}"
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)