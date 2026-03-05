import json
import os
PREFIXES = ["is_", "has_", "can_", "should_"]
def task_func(directory):
    # Initialize a dictionary to store the counts of keys with specified prefixes
    prefix_counts = {prefix: 0 for prefix in PREFIXES}
    
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
                            prefix_counts[prefix] += 1
                            break  # Break to avoid counting the same key multiple times
    
    return prefix_counts