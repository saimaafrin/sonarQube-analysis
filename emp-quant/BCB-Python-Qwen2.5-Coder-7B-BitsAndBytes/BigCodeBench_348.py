
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    # Find all process IDs (PIDs) associated with the given process name
    pids = [pid for pid, proc in psutil.process_iter(['pid', 'name']) if proc.name() == process_name]
    
    # Initialize a counter for the number of processes stopped
    stopped_count = 0
    
    # Send a termination signal to each process and wait for 1 second
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
            stopped_count += 1
        except OSError as e:
            print(f"Error stopping process {pid}: {e}")
    
    # Wait for up to 1 second for the processes to terminate
    time.sleep(1)
    
    # Check if any processes are still running
    remaining_pids = [pid for pid in pids if psutil.pid_exists(pid)]
    
    # Subtract the number of remaining processes from the total stopped count
    stopped_count -= len(remaining_pids)
    
    return stopped_count