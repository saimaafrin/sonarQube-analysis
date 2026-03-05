import subprocess
import time
import threading
def task_func(file_list):
    exit_codes = []
    threads = []

    def run_file(file):
        try:
            result = subprocess.run(['python', file], capture_output=True, text=True, check=True)
            exit_codes.append(result.returncode)
        except subprocess.CalledProcessError as e:
            exit_codes.append(e.returncode)

    for file in file_list:
        thread = threading.Thread(target=run_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return exit_codes