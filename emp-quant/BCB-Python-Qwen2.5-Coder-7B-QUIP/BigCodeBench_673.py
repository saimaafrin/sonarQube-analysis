
import os
import random

def task_func(directory, n_files):
    for i in range(1, n_files + 1):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, 'w') as file:
            random_digit = random.randint(0, 9)
            file.write(str(random_digit))
            file.seek(0)  # Reset cursor to the beginning of the file

    return n_files