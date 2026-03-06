
import subprocess
import time
import threading

def task_func(file_list):
    # Create a list to store the exit codes of the subprocesses
    exit_codes = []

    # Create a thread for each file in the list
    for file in file_list:
        # Create a new thread and pass the file name as an argument
        t = threading.Thread(target=run_file, args=(file,))
        # Start the thread
        t.start()
        # Append the thread to the list of threads
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Return the list of exit codes
    return exit_codes

def run_file(file_name):
    # Run the file as a subprocess
    p = subprocess.Popen(file_name, shell=True)
    # Wait for the process to finish
    p.wait()
    # Get the exit code of the process
    exit_code = p.returncode
    # Append the exit code to the list of exit codes
    exit_codes.append(exit_code)