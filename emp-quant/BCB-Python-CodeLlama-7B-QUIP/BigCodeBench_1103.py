
import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    try:
        # Create a temporary directory to run the script in
        os.makedirs(temp_dir, exist_ok=True)

        # Copy the script to the temporary directory
        shutil.copy(script_path, temp_dir)

        # Run the script
        subprocess.run(["python", script_path], cwd=temp_dir)

        # Return "Script executed successfully!"
        return "Script executed successfully!"
    except:
        # Return "Script execution failed!"
        return "Script execution failed!"