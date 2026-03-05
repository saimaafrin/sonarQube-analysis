
import subprocess
import shutil
import os
def task_func(script_path: str, temp_dir: str) -> str:
    # Ensure the temporary directory exists
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Copy the script to the temporary directory
    script_name = os.path.basename(script_path)
    temp_script_path = os.path.join(temp_dir, script_name)
    shutil.copy(script_path, temp_script_path)

    try:
        # Execute the script
        result = subprocess.run(['python', temp_script_path], capture_output=True, text=True)
        if result.returncode == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return f"Script execution failed with error: {e}"
    finally:
        # Clean up the temporary script file
        os.remove(temp_script_path)