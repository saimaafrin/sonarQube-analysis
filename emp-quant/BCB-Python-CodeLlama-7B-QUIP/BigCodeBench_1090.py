
import ast
import json
from collections import Counter

def task_func(file_pointer):
    # Read the JSON data from the file pointer
    data = json.load(file_pointer)

    # Create a Counter object to store the frequency of each key
    counter = Counter()

    # Loop through the dictionaries in the JSON data
    for d in data:
        # Evaluate the dictionary as a Python object
        d = ast.literal_eval(d)
        # Loop through the keys in the dictionary
        for key in d:
            # Increment the counter for the key
            counter[key] += 1

    return counter