
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Get a list of all running processes
    processes = subprocess.check_output(['ps', '-A']).decode('utf-8').splitlines()

    # Filter the list to only include processes with the specified name
    processes = [p for p in processes if process_name in p]

    # Send a termination signal to each process
    for p in processes:
        os.kill(int(p.split()[1]), signal.SIGTERM)

    # Wait for 1 second to allow processes to terminate
    time.sleep(1)

    # Get the number of processes that were stopped
    stopped_processes = len(processes)

    # Return the number of stopped processes
    return stopped_processes