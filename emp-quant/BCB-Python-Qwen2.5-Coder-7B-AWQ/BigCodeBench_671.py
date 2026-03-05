import os
import random
import json
def task_func(directory, n):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create n random files with json content
    for i in range(n):
        file_path = os.path.join(directory, f'file_{i}.json')
        with open(file_path, 'w') as file:
            data = {'number': random.randint(1, 100)}
            json.dump(data, file)
    
    # Reset the cursor to the beginning of each file
    for i in range(n):
        file_path = os.path.join(directory, f'file_{i}.json')
        with open(file_path, 'r+') as file:
            file.seek(0)
    
    return directory