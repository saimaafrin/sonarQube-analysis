
import os
import random
import json

def task_func(directory, n):
    # Create n random files in the directory with json content
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