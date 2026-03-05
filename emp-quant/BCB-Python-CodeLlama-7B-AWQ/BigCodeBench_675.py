import os
import random
def task_func(directory, n_files):
    """
    Create n random text files in a specific directory, write a random string to each file, and then reset the cursor to the beginning of each file.
    """
    # Create n random text files in the specified directory
    for i in range(n_files):
        file_name = f"{directory}/file_{i}.txt"
        with open(file_name, "w") as f:
            f.write(random.choice(string.ascii_letters))

    # Reset the cursor to the beginning of each file
    for i in range(n_files):
        file_name = f"{directory}/file_{i}.txt"
        with open(file_name, "r+") as f:
            f.seek(0)

    return directory
directory = "test_dir"
n_files = 5