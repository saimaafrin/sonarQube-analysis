
import subprocess
import time
import threading

def task_func(file_list):
    def run_file(file):
        result = subprocess.run(['python', file], capture_output=True, text=True)
        print(f"File {file} exited with code {result.returncode}")
        return result.returncode

    threads = []
    exit_codes = []

    for file in file_list:
        thread = threading.Thread(target=run_file, args=(file,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return exit_codes