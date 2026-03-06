import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified python code with a given timeout. If the script execution exceeds the timeout, it is terminated.

    Parameters:
    - script_path (str): The path to the Python code to be executed.
    - timeout (int): The maximum allowed time (in seconds) for the script execution. Default is 60 seconds.

    Returns:
    - str: A message indicating if the code was terminated due to timeout or executed successfully. The message is either "Script executed successfully." or "Terminating process due to timeout."

    Requirements:
    - subprocess
    - os
    - threading

    Examples:
    >>> task_func('/pathto/MyrScript.py')
    'Script executed successfully.'
    
    >>> task_func('/pathto/LongRunningScript.py', 30)
    'Terminating process due to timeout.'

    Note:
    - If the script was terminated due to timeout it will return "Script executed successfully.", otherwise "Terminating process due to timeout."

    Raise:
    - The code will raise FileNotFoundError if the file is not exist.
    """
    try:
        with open(script_path, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")

    # Create a thread to execute the code
    thread = threading.Thread(target=exec, args=(code,))
    thread.start()

    # Wait for the thread to finish
    thread.join(timeout)

    # If the thread is still running, terminate it
    if thread.is_alive():
        os.kill(thread.ident, 9)
        return "Terminating process due to timeout."

    return "Script executed successfully."