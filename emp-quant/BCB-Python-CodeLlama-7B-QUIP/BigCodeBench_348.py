
import subprocess
import os
import signal
import time

def task_func(process_name: str) -> int:
    processes = subprocess.Popen(["ps", "-A"], stdout=subprocess.PIPE)
    processes = processes.communicate()[0].split("\n")
    processes = [x for x in processes if process_name in x]
    if len(processes) == 0:
        return 0
    for process in processes:
        print(f"Stopping process: {process}")
        subprocess.Popen(["kill", process], stdout=subprocess.PIPE)
        time.sleep(1)
    return len(processes)