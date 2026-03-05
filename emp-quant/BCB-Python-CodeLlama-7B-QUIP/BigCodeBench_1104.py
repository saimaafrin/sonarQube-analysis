
import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified python code with a given timeout. If the script execution exceeds the timeout, it is terminated.
    :param script_path: The path to the python script to be executed
    :param timeout: The timeout in seconds
    :return: A message indicating if the code was terminated due to timeout or executed successfully.
    """
    try:
        # Start the script execution
        process = subprocess.Popen(script_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        # Create a thread to wait for the timeout
        thread = threading.Thread(target=lambda: time.sleep(timeout))
        thread.start()
        # Wait for the script to finish or the timeout
        process.wait(timeout)
        # Check if the script execution was terminated due to timeout
        if process.returncode == 0:
            return "Script executed successfully."
        else:
            return "Terminating process due to timeout."
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return "Error executing script"