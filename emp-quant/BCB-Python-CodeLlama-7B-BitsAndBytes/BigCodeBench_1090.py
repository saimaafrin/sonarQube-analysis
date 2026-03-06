
import ast
import json
from collections import Counter

def task_func(file_pointer):
    # Read the JSON data from the file pointer
    data = json.load(file_pointer)

    # Create an empty dictionary to store the counts
    counts = {}

    # Iterate over the data and count the frequency of each key
    for item in data:
        if isinstance(item, dict):
            for key, value in item.items():
                if key in counts:
                    counts[key] += 1
                else:
                    counts[key] = 1

    # Return the Counter object
    return Counter(counts)