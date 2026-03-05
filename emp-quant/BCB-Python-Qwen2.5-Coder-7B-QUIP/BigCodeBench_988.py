
import os
import re
from pathlib import Path
from typing import List, Dict

def task_func(dir_path: str, predicates: List[str]) -> Dict[str, bool]:
    # Check if the directory exists and is a directory
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise FileNotFoundError(f"The directory {dir_path} does not exist or is not a directory.")

    # Check if there are any valid predicates
    if not predicates:
        raise ValueError("No valid predicates provided.")

    # Initialize a dictionary to store the results
    results = {}

    # Iterate over the items in the directory
    for item in dir_path.iterdir():
        item_name = item.name
        # Check if the item name matches any of the predicates
        for predicate in predicates:
            if re.match(predicate, item_name):
                results[item_name] = True
                break
        else:
            results[item_name] = False

    return results