
import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    def run_script():
        try:
            result = subprocess.run(['python', script_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout, result.stderr
        except subprocess.CalledProcessError as e:
            return None, e.stderr

    def timeout_handler():
        print("Timeout occurred, terminating process.")
        os._exit(0)

    # Start the script in a separate thread
    script_thread = threading.Thread(target=run_script)
    script_thread.start()

    # Set a timeout for the script
    script_thread.join(timeout)

    if script_thread.is_alive():
        print("Terminating process due to timeout.")
        return "Terminating process due to timeout."

    # If the script completed within the timeout, return the result
    stdout, stderr = run_script()
    if stdout:
        return "Script executed successfully."
    else:
        return f"Error: {stderr.decode('utf-8')}"