
import subprocess
import time
import threading

def task_func(file_list):
    exit_codes = []
    threads = []

    def run_file(file):
        process = subprocess.Popen(['python', file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        exit_code = process.returncode
        exit_codes.append(exit_code)
        print(f"File {file} exited with code {exit_code}")

    for file in file_list:
        thread = threading.Thread(target=run_file, args=(file,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return exit_codes