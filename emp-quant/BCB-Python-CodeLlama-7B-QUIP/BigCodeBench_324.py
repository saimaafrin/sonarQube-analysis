
import subprocess
import time
import threading

def task_func(file_list):
    # Create a list to store the exit codes of the subprocesses
    exit_codes = []

    # Create a list to store the threads that will run the subprocesses
    threads = []

    # Loop through the files in the list
    for file in file_list:
        # Create a new thread to run the subprocess
        t = threading.Thread(target=subprocess.Popen, args=(file,))
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for all the threads to finish
    for t in threads:
        t.join()

    # Return the exit codes of the subprocesses
    return exit_codes