
import collections
import json
import os

def task_func(directory_path: str) -> dict:
    """
    Count the total appearances of all keys in all JSON files in the specified directory and return a dictionary with the keys from the JSON files as keys and their respective counts as values.
    """
    key_counts = collections.defaultdict(int)
    for filename in os.listdir(directory_path):
        with open(os.path.join(directory_path, filename), "r") as f:
            data = json.load(f)
            for key in data:
                key_counts[key] += 1
    return key_counts