import os
import hashlib
DIRECTORY = "./hashed_files"
def task_func(input_string):
    # Create the directory if it does not exist
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Split the input string into lines
    lines = input_string.splitlines()

    # Iterate over the lines and hash each non-empty line
    hashes = []
    for line in lines:
        if line:
            # Hash the line using SHA256
            hash = hashlib.sha256(line.encode()).hexdigest()

            # Save the hash to a file
            with open(os.path.join(DIRECTORY, hash[:10] + ".txt"), "w") as f:
                f.write(hash)

            # Add the file path to the list of hashes
            hashes.append(os.path.join(DIRECTORY, hash[:10] + ".txt"))

    return hashes
input_string = """
This is a multi-line string.

This line is empty.

This line is also empty.
"""