
import subprocess
import os
import sys
import time

def task_func(script_path, wait=True, *args):
    if not os.path.exists(script_path):
        raise ValueError("Script does not exist")
    try:
        process = subprocess.Popen(script_path, *args)
        if wait:
            output = process.wait()
            return output
        else:
            return None
    except subprocess.CalledProcessError as e:
        raise e