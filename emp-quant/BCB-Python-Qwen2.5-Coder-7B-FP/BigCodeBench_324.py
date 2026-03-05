import subprocess
import time
import threading
def task_func(file_list):
    exit_codes = []

    def run_file(file):
        result = subprocess.run(['python', file], capture_output=True, text=True)
        exit_codes.append(result.returncode)

    threads = []
    for file in file_list:
        thread = threading.Thread(target=run_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return exit_codes