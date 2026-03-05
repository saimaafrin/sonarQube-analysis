import os
import random
def task_func(directory, n_files):
    """
    Creates n random txt files in a specific directory, writes only a single digit random integer into each file, and then resets the cursor to the beginning of each file.
    The file names start from 'file_1.txt' and increment by 1 for each file.
    """
    # Create n random txt files in the specified directory
    for i in range(n_files):
        file_name = f"{directory}/file_{i+1}.txt"
        with open(file_name, "w") as f:
            f.write(str(random.randint(0, 9)))

    # Reset the cursor to the beginning of each file
    for i in range(n_files):
        file_name = f"{directory}/file_{i+1}.txt"
        with open(file_name, "r+") as f:
            f.seek(0)

    return n_files
directory = "./"
n_files = 5