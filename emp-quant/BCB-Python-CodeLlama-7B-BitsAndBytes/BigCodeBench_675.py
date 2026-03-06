
import os
import random

def task_func(directory, n_files):
    # Create n random text files in the specified directory
    for i in range(n_files):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as f:
            f.write(random.choice(string.ascii_letters) * 10)

    # Reset the cursor to the beginning of each file
    for i in range(n_files):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "r+") as f:
            f.seek(0)

    return directory