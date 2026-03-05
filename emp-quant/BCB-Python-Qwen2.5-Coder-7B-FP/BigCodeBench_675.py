import os
import random
import string
def task_func(directory, n_files):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # List to hold the file paths
    file_paths = []
    
    # Generate n random text files
    for i in range(n_files):
        # Create a random filename
        filename = ''.join(random.choices(string.ascii_letters, k=10)) + '.txt'
        file_path = os.path.join(directory, filename)
        
        # Write a random string to the file
        with open(file_path, 'w') as file:
            random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
            file.write(random_string)
        
        # Append the file path to the list
        file_paths.append(file_path)
    
    # Reset the cursor to the beginning of each file
    for file_path in file_paths:
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    # Return the directory where the files were generated
    return directory