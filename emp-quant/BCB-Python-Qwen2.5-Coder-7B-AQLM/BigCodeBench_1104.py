
import subprocess
import os
import threading

def task_func(script_path: str, timeout: int = 60) -> str:
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The file {script_path} does not exist.")
    
    process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    def kill_process():
        process.terminate()
        process.wait()
        return "Terminating process due to timeout."
    
    timer = threading.Timer(timeout, kill_process)
    timer.start()
    
    try:
        stdout, stderr = process.communicate()
        if process.returncode == 0:
            return "Script executed successfully."
        else:
            return f"Script execution failed with error: {stderr.decode('utf-8')}"
    finally:
        timer.cancel()