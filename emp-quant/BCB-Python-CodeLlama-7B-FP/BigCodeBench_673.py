import os
import random
def task_func(directory, n_files):
    """
    Create n random txt files in a specific directory, write only a single digit random integer into each file, and then reset the cursor to the beginning of each file. The file names start from 'file_1.txt' and increment by 1 for each file.
    The function should output with:
        n_files (int): The number of files generated.
    """
    # Create n random txt files in the specified directory
    for i in range(n_files):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as f:
            f.write(str(random.randint(0, 9)))

    # Reset the cursor to the beginning of each file
    for i in range(n_files):
        file_name = f"file_{i+1}.txt"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "r+") as f:
            f.seek(0)

    return n_files
directory = "./"
n_files = 5