import pandas as pd
from collections import Counter
def task_func(d):
    """
    Count the occurrence of values with the keys "x", "y", and "z" from a list of dictionaries "d".
    The function should output with:
        dict: A dictionary with keys as 'x', 'y', and 'z' and values as Counter objects.
    """
    # Create a dictionary to store the counts
    counts = {}

    # Iterate over the list of dictionaries
    for item in d:
        # Check if the key "x", "y", or "z" exists in the current dictionary
        if "x" in item:
            # Increment the count for "x"
            counts["x"] += 1
        if "y" in item:
            # Increment the count for "y"
            counts["y"] += 1
        if "z" in item:
            # Increment the count for "z"
            counts["z"] += 1

    # Return the counts dictionary
    return counts
d = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 4, "y": 5, "z": 6},
    {"x": 7, "y": 8, "z": 9},
    {"x": 10, "y": 11, "z": 12},
]