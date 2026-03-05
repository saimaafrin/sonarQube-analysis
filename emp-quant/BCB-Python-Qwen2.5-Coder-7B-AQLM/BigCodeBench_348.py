
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Find all processes with the given name
    process_ids = []
    for proc in subprocess.Popen(['pgrep', process_name], stdout=subprocess.PIPE).communicate()[0].split():
        process_ids.append(int(proc))

    # If no processes are found, return 0
    if not process_ids:
        return 0

    # Send a termination signal to each process and wait for 1 second
    for pid in process_ids:
        try:
            os.kill(pid, signal.SIGTERM)
            time.sleep(1)
        except OSError:
            pass

    # Return the number of processes stopped
    return len(process_ids)