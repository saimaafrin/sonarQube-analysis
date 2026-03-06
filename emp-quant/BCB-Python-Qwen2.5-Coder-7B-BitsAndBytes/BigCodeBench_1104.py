
import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    try:
        # Check if the script exists
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"The file {script_path} does not exist.")
        
        # Define a function to run the script
        def run_script():
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        
        # Create a thread to run the script
        script_thread = threading.Thread(target=run_script)
        script_thread.start()
        
        # Wait for the script to finish within the timeout period
        script_thread.join(timeout)
        
        # If the thread is still alive after the timeout, terminate it
        if script_thread.is_alive():
            print("Terminating process due to timeout.")
            return "Terminating process due to timeout."
        
        return "Script executed successfully."
    
    except Exception as e:
        return str(e)