import json
import os
PREFIXES = ["is_", "has_", "can_", "should_"]
def task_func(directory):
    # Initialize a dictionary to store the count of keys starting with each prefix
    prefix_counts = {prefix: 0 for prefix in PREFIXES}
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is a JSON file
        if filename.endswith('.json'):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Iterate over all keys in the JSON data
                for key in data.keys():
                    # Check if the key starts with any of the specified prefixes
                    for prefix in PREFIXES:
                        if key.startswith(prefix):
                            # Increment the count for the corresponding prefix
                            prefix_counts[prefix] += 1
                            break
    
    # Return the dictionary containing the counts of keys starting with each prefix
    return prefix_counts