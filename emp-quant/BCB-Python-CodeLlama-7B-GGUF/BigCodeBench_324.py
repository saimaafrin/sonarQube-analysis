
import subprocess
import time
import threading

def task_func(file_list):
    # Create a list to store the exit codes of the subprocesses
    exit_codes = []

    # Create a thread for each file in the list
    for file in file_list:
        # Create a new thread
        t = threading.Thread(target=run_file, args=(file,))
        # Add the thread to the list of threads
        threads.append(t)
        # Start the thread
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Return the list of exit codes
    return exit_codes

def run_file(file):
    # Run the file as a subprocess
    p = subprocess.Popen(file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # Wait for the subprocess to finish
    p.wait()
    # Get the exit code of the subprocess
    exit_code = p.returncode
    # Add the exit code to the list of exit codes
    exit_codes.append(exit_code)