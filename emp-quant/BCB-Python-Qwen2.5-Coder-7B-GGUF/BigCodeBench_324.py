
import subprocess
import time
import threading

def task_func(file_list):
    def run_file(file):
        process = subprocess.Popen(file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate(), process.returncode

    threads = []
    results = []

    for file in file_list:
        thread = threading.Thread(target=lambda f: results.append(run_file(f)), args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    exit_codes = [result[1] for result in results]
    return exit_codes