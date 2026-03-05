import subprocess
import time
import threading
def task_func(file_list):
    """
    Runs files from list of files as subprocesses at the same time.
    Returns a list of exit codes of the subprocesses.
    """
    # Create a list to store the exit codes
    exit_codes = []

    # Create a list of threads
    threads = []

    # Iterate over the file list
    for file in file_list:
        # Create a new thread for each file
        t = threading.Thread(target=subprocess.run, args=(file,))
        threads.append(t)

    # Start all the threads
    for t in threads:
        t.start()

    # Wait for all the threads to finish
    for t in threads:
        t.join()

    # Get the exit codes of the subprocesses
    for t in threads:
        exit_codes.append(t.exitcode)

    return exit_codes
file_list = ['file1.txt', 'file2.txt', 'file3.txt']