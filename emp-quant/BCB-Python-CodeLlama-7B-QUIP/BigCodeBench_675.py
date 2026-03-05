
import os
import random

def task_func(directory, n_files):
    for i in range(n_files):
        file_name = f"{directory}/file_{i}.txt"
        with open(file_name, "w") as f:
            f.write(random.choice(string.ascii_letters))
        f.seek(0)
    return directory