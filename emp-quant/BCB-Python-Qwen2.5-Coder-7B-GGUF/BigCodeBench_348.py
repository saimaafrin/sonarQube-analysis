
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Find all processes with the given name
    process_ids = []
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            process_ids.append(proc.info['pid'])
    
    # If no processes are found, return 0
    if not process_ids:
        return 0
    
    # Send termination signal to each process and wait for 1 second
    for pid in process_ids:
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            continue
    
    time.sleep(1)
    
    # Check if processes are still running and count the number of stopped processes
    stopped_count = 0
    for pid in process_ids:
        try:
            if psutil.pid_exists(pid):
                continue
            stopped_count += 1
        except ProcessLookupError:
            continue
    
    return stopped_count