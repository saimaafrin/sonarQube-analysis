
import json
import os

# Constants
PREFIXES = ["is_", "has_", "can_", "should_"]

def task_func(directory):
    # Initialize a dictionary to store the counts
    counts = {prefix: 0 for prefix in PREFIXES}
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                
                # Check each key in the JSON data
                for key in data.keys():
                    for prefix in PREFIXES:
                        if key.startswith(prefix):
                            counts[prefix] += 1
                            break
    
    return counts