
import subprocess
import os
import sys
import time
def task_func(script_path, wait=True, *args):
    if not os.path.exists(script_path):
        raise ValueError("Script does not exist")
    
    try:
        result = subprocess.run([script_path] + list(args), capture_output=True, text=True)
        if not wait:
            return None
        return result.returncode
    except subprocess.CalledProcessError as e:
        raise e