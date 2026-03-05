import os
import random
def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Loop to create n_files
    for i in range(1, n_files + 1):
        # Create file name
        file_name = f'file_{i}.txt'
        file_path = os.path.join(directory, file_name)
        
        # Write a random digit to the file
        with open(file_path, 'w') as file:
            file.write(str(random.randint(0, 9)))
        
        # Reset the cursor to the beginning of the file
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    # Return the number of files generated
    return n_files