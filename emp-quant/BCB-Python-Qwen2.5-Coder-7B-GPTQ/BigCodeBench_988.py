import os
import re
from pathlib import Path
def task_func(dir_path: str, predicates: list) -> dict:
    # Check if predicates are provided
    if not predicates:
        raise ValueError("No valid predicates provided.")
    
    # Check if the specified directory exists and is a directory
    if not Path(dir_path).is_dir():
        raise FileNotFoundError("The specified directory does not exist or is not a directory.")
    
    # Initialize the result dictionary
    results = {}
    
    # Iterate over each item in the directory
    for item in os.listdir(dir_path):
        # Check each predicate against the item name
        for predicate in predicates:
            # Use regular expression to match the predicate
            if re.match(predicate, item):
                results[item] = True
                break
        else:
            results[item] = False
    
    return results