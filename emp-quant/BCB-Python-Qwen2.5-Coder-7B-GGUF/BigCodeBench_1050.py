
import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Ensure the directory exists
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # List to store file paths
    file_paths = []

    # Split the input string into lines
    lines = input_string.strip().split('\n')

    # Process each non-empty line
    for line in lines:
        if line:
            # Hash the line using SHA256
            hash_object = hashlib.sha256(line.encode())
            hex_dig = hash_object.hexdigest()

            # Create the filename
            filename = hex_dig[:10] + '.txt'

            # Create the file path
            file_path = os.path.join(DIRECTORY, filename)

            # Write the hash to the file
            with open(file_path, 'w') as file:
                file.write(hex_dig)

            # Add the file path to the list
            file_paths.append(file_path)

    return file_paths