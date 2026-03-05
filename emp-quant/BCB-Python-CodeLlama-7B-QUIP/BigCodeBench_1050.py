
import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Create the directory if it doesn't exist
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)

    # Iterate over each line in the input string
    for line in input_string.splitlines():
        # Ignore empty lines
        if line == "":
            continue

        # Hash the line and save it to a file
        hash_object = hashlib.sha256(line.encode())
        filename = hash_object.hexdigest()[:10] + ".txt"
        with open(os.path.join(DIRECTORY, filename), "w") as f:
            f.write(line)

    # Return the list of file paths
    return [os.path.join(DIRECTORY, filename) for filename in os.listdir(DIRECTORY)]