
import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None
    file_name = random.choice(file_list)
    file_path = os.path.join(directory, file_name)
    try:
        process = subprocess.Popen(file_path)
        return process.returncode
    except OSError:
        return None