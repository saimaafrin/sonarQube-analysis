
import subprocess
import os
import sys
import glob

def task_func(directory_path):
    files = glob.glob(directory_path + "/*.bat")
    results = []
    for file in files:
        try:
            result = subprocess.run(file, shell=True)
            results.append((file, result.returncode))
        except OSError:
            results.append((file, None))
    return results