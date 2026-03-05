import os
import random
import json
def task_func(directory, n):
    """
    Create n random files in a directory with json content with the key 'number' and a random integer value between 1 and 100, and then reset the cursor to the beginning of each file.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(n):
        file_name = f"{directory}/file_{i}.json"
        with open(file_name, "w") as f:
            json.dump({"number": random.randint(1, 100)}, f)
        with open(file_name, "r") as f:
            f.seek(0)
    return directory