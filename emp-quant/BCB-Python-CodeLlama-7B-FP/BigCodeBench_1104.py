import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified Python code with a given timeout. If the script execution exceeds the timeout, it is terminated.
    :param script_path: The path to the Python script to be executed.
    :param timeout: The maximum time in seconds to allow the script to run.
    :return: A message indicating if the code was terminated due to timeout or executed successfully.
    """
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"File {script_path} does not exist.")

    # Create a thread to run the script in the background.
    thread = threading.Thread(target=subprocess.run, args=(script_path,))
    thread.start()

    # Wait for the script to finish or the timeout to be reached.
    thread.join(timeout)

    # Check if the script was terminated due to timeout.
    if thread.is_alive():
        thread.terminate()
        return "Terminating process due to timeout."
    else:
        return "Script executed successfully."
script_path = "/pathto/LongRunningScript.py"
timeout = 30