import subprocess
import os
import signal
import time
def task_func(process_name: str) -> int:
    """
    Stops all running processes with a specific name.
    Note that:
        - The function sends a termination signal to the processes and waits for 1 second.
        - There is no guarantee that all processes will have terminated within this time.
        - The function should output with:
            - int: The number of processes stopped. If no processes are found, returns 0.
    """
    # Get the list of all running processes
    processes = subprocess.check_output(['ps', 'aux']).decode('utf-8').split('\n')

    # Filter the list to get only the processes with the specified name
    processes = [process for process in processes if process_name in process]

    # Send a termination signal to each process
    for process in processes:
        os.kill(int(process.split()[1]), signal.SIGTERM)

    # Wait for 1 second
    time.sleep(1)

    # Get the list of all running processes again
    processes = subprocess.check_output(['ps', 'aux']).decode('utf-8').split('\n')

    # Filter the list to get only the processes with the specified name
    processes = [process for process in processes if process_name in process]

    # Return the number of processes stopped
    return len(processes)