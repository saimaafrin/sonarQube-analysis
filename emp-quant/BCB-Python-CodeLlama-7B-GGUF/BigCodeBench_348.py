
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Get a list of all running processes
    processes = subprocess.check_output(['ps', 'aux']).decode().split('\n')

    # Filter the list to only include processes with the specified name
    processes = [process for process in processes if process_name in process]

    # Send a termination signal to each process
    for process in processes:
        os.kill(int(process.split()[1]), signal.SIGTERM)

    # Wait for 1 second to allow processes to terminate
    time.sleep(1)

    # Get the number of processes that were stopped
    stopped_processes = len([process for process in processes if process.split()[1] in subprocess.check_output(['ps', 'aux']).decode().split('\n')])

    return stopped_processes