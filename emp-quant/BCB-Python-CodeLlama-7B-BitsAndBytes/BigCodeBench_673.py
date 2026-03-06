
import os
import random

def task_func(directory, n_files):
    for i in range(n_files):
        file_name = f"{directory}/file_{i+1}.txt"
        with open(file_name, "w") as f:
            f.write(str(random.randint(0, 9)))
        f.seek(0)
    return n_files