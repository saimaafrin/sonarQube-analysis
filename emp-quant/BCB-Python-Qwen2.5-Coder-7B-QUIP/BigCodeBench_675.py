
import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # List to hold the file names
    file_names = []

    # Generate n random text files
    for _ in range(n_files):
        # Generate a random file name
        file_name = f"file_{random.randint(1, 1000)}.txt"
        file_names.append(file_name)

        # Open the file and write a random string
        with open(os.path.join(directory, file_name), 'w') as file:
            file.write(str(random.randint(1, 1000)))

    # Reset the cursor to the beginning of each file
    for file_name in file_names:
        with open(os.path.join(directory, file_name), 'r+') as file:
            file.seek(0)

    return directory