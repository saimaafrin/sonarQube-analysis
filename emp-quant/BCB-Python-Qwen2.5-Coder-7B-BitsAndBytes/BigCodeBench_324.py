
import subprocess
import time
import threading

def task_func(file_list):
    def run_subprocess(file_path):
        try:
            result = subprocess.run(['python', file_path], capture_output=True, text=True)
            print(f"File {file_path} exited with code {result.returncode}")
            return result.returncode
        except Exception as e:
            print(f"Error running {file_path}: {e}")
            return None

    threads = []
    results = []

    for file_path in file_list:
        thread = threading.Thread(target=run_subprocess, args=(file_path,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        results.append(thread.result)

    return results