
import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None
    file_path = os.path.join(directory, random.choice(file_list))
    process = subprocess.Popen(file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    return process.returncode