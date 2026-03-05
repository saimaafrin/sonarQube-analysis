import subprocess
import os
import signal
import time
def task_func(process_name: str) -> int:
    # Find all processes with the given name
    result = subprocess.run(['pgrep', process_name], stdout=subprocess.PIPE)
    process_ids = result.stdout.decode().splitlines()
    
    # If no processes are found, return 0
    if not process_ids:
        return 0
    
    # Send a termination signal to each process and wait for 1 second
    for pid in process_ids:
        try:
            os.kill(int(pid), signal.SIGTERM)
            time.sleep(1)
        except ProcessLookupError:
            # Process might have terminated before we could send the signal
            continue
    
    # Return the number of processes stopped
    return len(process_ids)