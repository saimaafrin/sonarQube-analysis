
import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified Python script with a given timeout.
    If the script execution exceeds the timeout, it is terminated.
    """
    # Check if the script file exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"Script file {script_path} does not exist.")

    # Create a new process and thread
    process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE)
    thread = threading.Thread(target=process.communicate, args=(timeout,))

    # Start the thread
    thread.start()

    # Wait for the thread to finish or timeout
    thread.join(timeout)

    # Check if the thread finished successfully
    if thread.is_alive():
        # Terminate the process
        process.terminate()
        return "Terminating process due to timeout."
    else:
        # Get the output from the process
        output = process.stdout.read().decode("utf-8")
        return "Script executed successfully."