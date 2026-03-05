
import subprocess
import os
import sys
import time

def task_func(script_path, wait=True, *args):
    if not os.path.exists(script_path):
        raise ValueError(f"Script {script_path} does not exist")
    try:
        process = subprocess.Popen([script_path, *args])
        if wait:
            process.wait()
            return process.returncode
        else:
            return None
    except subprocess.CalledProcessError as e:
        raise ValueError(f"Script {script_path} raised an exception: {e}")