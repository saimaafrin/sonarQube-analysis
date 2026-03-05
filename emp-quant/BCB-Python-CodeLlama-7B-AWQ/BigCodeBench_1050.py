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
    hashed_lines = []
    for line in lines:
        if line:
            # Hash the line using SHA256
            hash_object = hashlib.sha256(line.encode())
            hash_digest = hash_object.hexdigest()

            # Save the hash to a file
            file_path = os.path.join(DIRECTORY, hash_digest[:10] + ".txt")
            with open(file_path, "w") as f:
                f.write(hash_digest)

            # Add the file path to the list of hashed lines
            hashed_lines.append(file_path)

    return hashed_lines
input_string = """
This is a test string.

This is another test string.

This is a third test string.
"""