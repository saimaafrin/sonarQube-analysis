
import os
import re
from pathlib import Path

def task_func(dir_path: str, predicates: list) -> dict:
    if not predicates:
        raise ValueError("No valid predicates provided")
    if not os.path.exists(dir_path) or not os.path.isdir(dir_path):
        raise FileNotFoundError(f"Directory {dir_path} does not exist or is not a directory")

    # Create a dictionary to store the results of the condition checks
    results = {}

    # Iterate over the predicates and check each item in the directory against the predicate
    for predicate in predicates:
        # Get the items in the directory that match the predicate
        items = [item for item in os.listdir(dir_path) if re.match(predicate, item)]

        # Check the items against the predicate and add the results to the results dictionary
        for item in items:
            results[item] = predicate(item)

    return results