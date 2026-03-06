
import subprocess
import psutil
import time
import os

def task_func(script_path: str, timeout=10) -> dict:
    # Check if the script path exists
    if not os.path.exists(script_path):
        raise FileNotFoundError(f"The script {script_path} does not exist.")
    
    cpu_usage = 0
    memory_usage = 0
    
    try:
        # Start the subprocess
        process = subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        start_time = time.time()
        
        while True:
            # Check if the process has finished
            if process.poll() is not None:
                break
            
            # Check if the process has become a zombie
            if process.returncode is not None:
                raise Exception("The process has become a zombie.")
            
            # Get the current process
            proc = psutil.Process(process.pid)
            
            # Accumulate CPU and memory usage
            cpu_usage += proc.cpu_percent(interval=None)
            memory_usage += proc.memory_info().rss
            
            # Check if the timeout has been reached
            if time.time() - start_time > timeout:
                process.terminate()
                raise TimeoutError("The script execution exceeded the timeout.")
            
            # Sleep for a short interval
            time.sleep(0.1)
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {'CPU Usage': cpu_usage, 'Memory Usage': memory_usage}
    
    finally:
        # Ensure the subprocess is terminated
        if process.poll() is None:
            process.terminate()
    
    return {'CPU Usage': cpu_usage, 'Memory Usage': memory_usage}