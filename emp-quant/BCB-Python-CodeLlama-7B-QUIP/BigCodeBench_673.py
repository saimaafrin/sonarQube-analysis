
import os
import random

def task_func(directory, n_files):
    for i in range(n_files):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as f:
            f.write(str(random.randint(1, 10)))
        f.seek(0)
    return n_files