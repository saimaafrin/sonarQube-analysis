import subprocess
import time
import threading
def task_func(file_list):
    """
    Run files from list of files as subprocesses at the same time.
    The function should output with:
        list: The exit codes of the subprocesses.
    """
    # Create a list to store the exit codes of the subprocesses
    exit_codes = []

    # Create a list of threads to run the subprocesses
    threads = []

    # Iterate over the list of files
    for file in file_list:
        # Create a new thread to run the subprocess
        t = threading.Thread(target=subprocess.run, args=(file,))
        # Add the thread to the list of threads
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Get the exit codes of the subprocesses
    for t in threads:
        exit_codes.append(t.exitcode)

    # Return the list of exit codes
    return exit_codes
file_list = ["file1.txt", "file2.txt", "file3.txt"]