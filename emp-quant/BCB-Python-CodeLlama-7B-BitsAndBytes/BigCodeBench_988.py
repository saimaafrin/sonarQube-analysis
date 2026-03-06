
import os
import re
from pathlib import Path

def task_func(dir_path: str, predicates: list) -> dict:
    """
    Evaluates each item (files and directories) in a given directory against specified conditions.

    Args:
        dir_path (str): The path to the directory to be evaluated.
        predicates (list): A list of predicates to be applied to the directory items.

    Returns:
        dict: A dictionary with directory items as keys and the results of condition checks as values.

    Raises:
        ValueError: If no valid predicates are provided.
        FileNotFoundError: If the specified directory does not exist or is not a directory.
    """
    if not predicates:
        raise ValueError("No valid predicates provided.")

    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise FileNotFoundError(f"Directory {dir_path} does not exist or is not a directory.")

    results = {}
    for item in dir_path.iterdir():
        for predicate in predicates:
            if predicate(item):
                results[item] = True
            else:
                results[item] = False

    return results