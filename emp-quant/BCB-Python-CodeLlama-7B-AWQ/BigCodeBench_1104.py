import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Executes the specified Python script with a given timeout.
    If the script execution exceeds the timeout, it is terminated.
    """
    # Create a thread to run the script
    thread = threading.Thread(target=subprocess.run, args=(script_path,))
    thread.start()

    # Wait for the script to finish or timeout
    thread.join(timeout)

    # Check if the script was terminated due to timeout
    if thread.is_alive():
        # Terminate the script
        thread.terminate()
        return "Terminating process due to timeout."
    else:
        # Script executed successfully
        return "Script executed successfully."