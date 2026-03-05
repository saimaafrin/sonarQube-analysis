import subprocess
import shutil
import os
def task_func(script_path: str, temp_dir: str) -> str:
    """
    Execute a given Python code in a temporary directory.
    Returns "Script executed successfully!" if the Python code can be run successfully,
    otherwise "Script execution failed!"
    """
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()

    # Copy the script to the temporary directory
    shutil.copy(script_path, temp_dir)

    # Change the current working directory to the temporary directory
    os.chdir(temp_dir)

    # Run the script
    try:
        subprocess.check_call([sys.executable, script_path])
        return "Script executed successfully!"
    except subprocess.CalledProcessError:
        return "Script execution failed!"
    finally:
        # Remove the temporary directory
        shutil.rmtree(temp_dir)