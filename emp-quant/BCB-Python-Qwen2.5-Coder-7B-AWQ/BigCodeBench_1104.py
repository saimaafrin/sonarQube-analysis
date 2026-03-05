import subprocess
import os
import threading
def task_func(script_path: str, timeout: int = 60) -> str:
    # Check if the script exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script at {script_path} does not exist.")
    
    # Function to run the script
    def run_script():
        try:
            # Execute the script using subprocess
            result = subprocess.run(['python', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr.decode('utf-8')}"
    
    # Function to handle the timeout
    def timeout_handler():
        raise TimeoutError("Script execution exceeded the timeout.")
    
    # Create a thread to run the script
    script_thread = threading.Thread(target=run_script)
    script_thread.start()
    
    # Create a thread to handle the timeout
    timeout_thread = threading.Thread(target=timeout_handler)
    timeout_thread.start()
    
    # Wait for the script thread to finish or the timeout thread to raise an exception
    script_thread.join(timeout)
    timeout_thread.join()
    
    # Check if the script thread is still alive
    if script_thread.is_alive():
        return "Terminating process due to timeout."
    else:
        return "Script executed successfully."