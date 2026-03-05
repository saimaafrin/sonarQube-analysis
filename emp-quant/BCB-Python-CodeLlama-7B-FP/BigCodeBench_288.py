import collections
import json
import os
def task_func(directory_path: str) -> dict:
    """
    Count the total appearances of all keys in all JSON files in the specified directory and return a dictionary with the keys from the JSON files as keys and their respective counts as values.
    """
    # Create an empty dictionary to store the counts
    counts = collections.defaultdict(int)

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        # Open the file and read its contents
        with open(os.path.join(directory_path, filename), "r") as f:
            data = json.load(f)

        # Iterate over all keys in the JSON data
        for key in data:
            # Increment the count for the current key
            counts[key] += 1

    # Return the dictionary with the counts
    return counts
directory_path = "path/to/directory"