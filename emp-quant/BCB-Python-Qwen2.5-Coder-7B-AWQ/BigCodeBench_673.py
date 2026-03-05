import os
import random
def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Loop to create n_files
    for i in range(1, n_files + 1):
        # Create file name
        file_name = os.path.join(directory, f'file_{i}.txt')
        
        # Open file in write mode and write a random digit
        with open(file_name, 'w') as file:
            file.write(str(random.randint(0, 9)))
        
        # Reset the cursor to the beginning of the file
        with open(file_name, 'r+') as file:
            file.seek(0)

    # Return the number of files generated
    return n_files