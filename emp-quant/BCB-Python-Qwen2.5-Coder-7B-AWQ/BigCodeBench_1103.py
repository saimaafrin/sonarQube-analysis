import subprocess
import shutil
import os
def task_func(script_path: str, temp_dir: str) -> str:
    # Create a temporary directory if it doesn't exist
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Copy the script to the temporary directory
    shutil.copy(script_path, temp_dir)

    # Change the current working directory to the temporary directory
    original_cwd = os.getcwd()
    os.chdir(temp_dir)

    try:
        # Execute the script using subprocess
        result = subprocess.run(['python', os.path.basename(script_path)], capture_output=True, text=True)
        
        # Check if the script executed successfully
        if result.returncode == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return f"Script execution failed with error: {str(e)}"
    finally:
        # Change back to the original working directory
        os.chdir(original_cwd)
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)