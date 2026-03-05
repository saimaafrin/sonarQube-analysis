
import ast
import json
from collections import Counter

def task_func(file_pointer):
    # Initialize a Counter to store the frequency of each key
    key_counter = Counter()

    # Read the file line by line
    for line in file_pointer:
        # Evaluate the line as a dictionary
        dictionary = ast.literal_eval(line)
        # Update the Counter with the keys from the dictionary
        key_counter.update(dictionary.keys())

    # Return the Counter object
    return key_counter