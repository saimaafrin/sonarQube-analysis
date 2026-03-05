
import os
import hashlib
# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Ensure the directory exists
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Split the input string into lines
    lines = input_string.split('\n')

    # Filter out empty lines
    non_empty_lines = [line for line in lines if line.strip() != '']

    # Initialize a list to store the file paths
    file_paths = []

    # Process each non-empty line
    for line in non_empty_lines:
        # Hash the line using SHA256
        hash_object = hashlib.sha256(line.encode())
        hash_value = hash_object.hexdigest()

        # Create the filename with the first 10 characters of the hash
        filename = hash_value[:10] + '.txt'

        # Full file path
        file_path = os.path.join(DIRECTORY, filename)

        # Save the hash to the file
        with open(file_path, 'w') as file:
            file.write(hash_value)

        # Add the file path to the list
        file_paths.append(file_path)

    return file_paths