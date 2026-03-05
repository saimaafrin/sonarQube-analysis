import subprocess
import os
import random
def task_func(directory, file_list):
    """
    Select a random file from a given list of files in a specified directory and run it as a subprocess.
    The function should output with:
        int: The exit code of the subprocess, or None if the process is still running or if the file list is empty.
    """
    if not file_list:
        return None
    file_path = os.path.join(directory, random.choice(file_list))
    process = subprocess.Popen(file_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()
    return process.returncode