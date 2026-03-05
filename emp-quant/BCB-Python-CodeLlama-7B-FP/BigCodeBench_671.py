import os
import random
import json
def task_func(directory, n):
    """
    Create n random files in a directory with json content with the key 'number' and a random integer value between 1 and 100, and then reset the cursor to the beginning of each file.
    The function should output with:
        directory (str): The directory in which the files were generated.
    """
    # Create n random files in the directory
    for i in range(n):
        file_name = f"file_{i}.json"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "w") as f:
            json.dump({"number": random.randint(1, 100)}, f)

    # Reset the cursor to the beginning of each file
    for i in range(n):
        file_name = f"file_{i}.json"
        file_path = os.path.join(directory, file_name)
        with open(file_path, "r+") as f:
            f.seek(0)

    # Output the directory
    return directory
directory = "test_dir"
n = 5