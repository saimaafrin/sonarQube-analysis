import pandas as pd
from collections import Counter
def task_func(d):
    """
    Count the occurrence of values with the keys "x," "y" and "z" from a list of dictionaries "d."
    The function should output with:
        dict: A dictionary with keys as 'x', 'y', and 'z' and values as Counter objects.
    """
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the list of dictionaries
    for dictionary in d:
        # Iterate over the keys in the current dictionary
        for key in dictionary:
            # If the key is "x", "y", or "z", increment the count
            if key in ["x", "y", "z"]:
                counts[key] = counts.get(key, 0) + 1

    # Return the counts dictionary
    return counts
d = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 4, "y": 5, "z": 6},
    {"x": 7, "y": 8, "z": 9},
]