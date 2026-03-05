
import os
import random

def task_func(directory, n_files):
    for i in range(1, n_files+1):
        file_name = f"file_{i}.txt"
        with open(os.path.join(directory, file_name), "w") as f:
            f.write(str(random.randint(0, 9)))
        f.seek(0)
    return n_files