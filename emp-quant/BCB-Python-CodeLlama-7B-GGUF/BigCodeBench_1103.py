
import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Copy the script to the temporary directory
    shutil.copy(script_path, temp_dir)

    # Change the current working directory to the temporary directory
    os.chdir(temp_dir)

    # Execute the script
    try:
        subprocess.run(["python", script_path], check=True)
        return "Script executed successfully!"
    except subprocess.CalledProcessError:
        return "Script execution failed!"