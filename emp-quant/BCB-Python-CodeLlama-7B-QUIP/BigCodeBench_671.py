
import os
import random
import json

def task_func(directory, n):
    for i in range(n):
        file_name = f"{directory}/file_{i}.json"
        with open(file_name, "w") as f:
            json.dump({"number": random.randint(1, 100)}, f)
        f.seek(0)
    return directory