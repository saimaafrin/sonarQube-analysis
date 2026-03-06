
import os
import random
import json

def task_func(directory, n):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n):
        filename = f"file_{i}.json"
        filepath = os.path.join(directory, filename)
        
        # Create a dictionary with a random number
        data = {'number': random.randint(1, 100)}
        
        # Write the JSON data to the file
        with open(filepath, 'w') as file:
            json.dump(data, file)
        
        # Reset the cursor to the beginning of the file
        with open(filepath, 'r+') as file:
            file.seek(0)

    return directory