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
    :param process_name: The name of the process to stop.
    :return: The number of processes stopped. If no processes are found, returns 0.
    """
    # Get the list of running processes
    running_processes = subprocess.check_output(["ps", "aux"]).decode("utf-8").split("\n")

    # Filter the list to only include processes with the specified name
    filtered_processes = [process for process in running_processes if process_name in process]

    # Send a termination signal to each process
    for process in filtered_processes:
        os.kill(int(process.split()[1]), signal.SIGTERM)

    # Wait for 1 second to allow processes to terminate
    time.sleep(1)

    # Get the list of running processes again
    running_processes = subprocess.check_output(["ps", "aux"]).decode("utf-8").split("\n")

    # Count the number of processes that are still running
    num_stopped = len(running_processes) - len(filtered_processes)

    return num_stopped
process_name = "python"