import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified Python script with a given timeout. If the script execution exceeds the timeout,
    it is terminated. If the script is terminated due to timeout, it returns "Terminating process due to timeout."
    If the script executes successfully within the timeout, it returns "Script executed successfully."
    
    :param script_path: Path to the Python script to be executed.
    :param timeout: Maximum time in seconds for the script to execute.
    :return: A message indicating if the script was terminated due to timeout or executed successfully.
    """
    # Check if the script file exists
    if not os.path.isfile(script_path):
        raise FileNotFoundError(f"The script file {script_path} does not exist.")
    
    # Function to run the script
    def run_script():
        try:
            # Execute the script using subprocess
            result = subprocess.run(['python', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr.decode('utf-8')}"
    
    # Create a thread to run the script
    script_thread = threading.Thread(target=run_script)
    script_thread.start()
    
    # Wait for the script to complete or timeout
    script_thread.join(timeout)
    
    # Check if the script is still running
    if script_thread.is_alive():
        # Terminate the script
        script_thread._stop()
        return "Terminating process due to timeout."
    else:
        # Return the result of the script execution
        return "Script executed successfully."