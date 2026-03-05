import os
import hashlib
DIRECTORY = "./hashed_files"
def task_func(input_string):
    # Create the directory if it does not exist
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Initialize a list to store the file paths
    file_paths = []

    # Split the input string into lines
    lines = input_string.split('\n')

    # Iterate over each line
    for line in lines:
        # Ignore empty lines
        if line.strip():
            # Hash the line using SHA256
            sha256_hash = hashlib.sha256(line.encode()).hexdigest()

            # Create the filename using the first 10 characters of the hash
            filename = sha256_hash[:10] + '.txt'

            # Create the full file path
            file_path = os.path.join(DIRECTORY, filename)

            # Write the hash to the file
            with open(file_path, 'w') as file:
                file.write(sha256_hash)

            # Add the file path to the list
            file_paths.append(file_path)

    # Return the list of file paths
    return file_paths