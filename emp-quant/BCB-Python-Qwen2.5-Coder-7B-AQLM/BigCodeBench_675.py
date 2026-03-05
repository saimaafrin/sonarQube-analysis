
import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # List of characters to use in the random strings
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # Create n random text files and write random strings to each
    for i in range(n_files):
        file_path = os.path.join(directory, f'file_{i}.txt')
        with open(file_path, 'w') as file:
            random_string = ''.join(random.choices(characters, k=10))
            file.write(random_string)

        # Reset the cursor to the beginning of the file
        with open(file_path, 'r+') as file:
            file.seek(0)

    return directory