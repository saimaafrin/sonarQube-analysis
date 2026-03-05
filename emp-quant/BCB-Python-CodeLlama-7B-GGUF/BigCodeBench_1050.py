
import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Create the directory if it doesn't exist
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Split the input string into lines
    lines = input_string.splitlines()

    # Iterate over the lines and hash each non-empty one
    hashed_lines = []
    for line in lines:
        if line.strip():
            # Calculate the SHA256 hash of the line
            hash_value = hashlib.sha256(line.encode()).hexdigest()
            # Save the hash to a file
            with open(os.path.join(DIRECTORY, hash_value[:10] + ".txt"), "w") as f:
                f.write(hash_value)
            # Add the file path to the list of hashed lines
            hashed_lines.append(os.path.join(DIRECTORY, hash_value[:10] + ".txt"))

    return hashed_lines