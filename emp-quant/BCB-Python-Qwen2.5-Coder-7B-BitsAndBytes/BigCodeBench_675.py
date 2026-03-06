
import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        # Create a random filename
        filename = f"file_{i}.txt"
        filepath = os.path.join(directory, filename)
        
        # Write a random string to the file
        random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
        with open(filepath, 'w') as file:
            file.write(random_string)
        
        # Reset the cursor to the beginning of the file
        with open(filepath, 'r+') as file:
            file.seek(0)

    return directory