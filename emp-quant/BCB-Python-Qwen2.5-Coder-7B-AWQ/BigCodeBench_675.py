import os
import random
def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # List to hold the file paths
    file_paths = []

    # Generate n random text files and write a random string to each
    for i in range(n_files):
        file_path = os.path.join(directory, f"file_{i}.txt")
        with open(file_path, 'w') as file:
            random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
            file.write(random_string)
        file_paths.append(file_path)

    # Reset the cursor to the beginning of each file
    for file_path in file_paths:
        with open(file_path, 'r+') as file:
            file.seek(0)

    return directory