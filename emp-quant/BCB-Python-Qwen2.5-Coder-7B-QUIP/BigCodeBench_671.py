
import os
import random
import json
def task_func(directory, n):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for _ in range(n):
        filename = f"file{_}.json"
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as file:
            data = {'number': random.randint(1, 100)}
            json.dump(data, file)
            file.seek(0)  # Reset cursor to the beginning of the file
    
    return directory