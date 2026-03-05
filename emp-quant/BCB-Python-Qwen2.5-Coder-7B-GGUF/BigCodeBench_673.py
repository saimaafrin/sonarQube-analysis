
import os
import random

def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate n random txt files
    for i in range(1, n_files + 1):
        file_path = os.path.join(directory, f'file_{i}.txt')
        with open(file_path, 'w') as file:
            # Write a single random digit to each file
            random_digit = str(random.randint(0, 9))
            file.write(random_digit)
        
        # Reset the cursor to the beginning of each file
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    return n_files