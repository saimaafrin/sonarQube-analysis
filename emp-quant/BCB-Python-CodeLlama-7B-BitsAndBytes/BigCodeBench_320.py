
import subprocess
import os
import random

def task_func(directory, file_list):
    if not file_list:
        return None
    file_name = random.choice(file_list)
    file_path = os.path.join(directory, file_name)
    process = subprocess.Popen(file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    exit_code = process.returncode
    return exit_code