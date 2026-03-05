
import os
import re
from pathlib import Path

def task_func(dir_path: str, predicates: list) -> dict:
    """
    Evaluates each item (files and directories) in a given directory against specified conditions.

    Args:
        dir_path (str): Path to the directory to be evaluated.
        predicates (list): List of predicates to be applied to the directory items.

    Returns:
        dict: A dictionary with directory items as keys and the results of condition checks as values.

    Raises:
        ValueError: If no valid predicates are provided.
        FileNotFoundError: If the specified directory does not exist or is not a directory.
    """
    if not predicates:
        raise ValueError("No valid predicates provided.")

    if not os.path.isdir(dir_path):
        raise FileNotFoundError(f"Directory '{dir_path}' does not exist or is not a directory.")

    results = {}
    for item in os.scandir(dir_path):
        if item.is_file():
            file_path = Path(item.path)
            for predicate in predicates:
                if predicate(file_path):
                    results[file_path] = True
                    break
        elif item.is_dir():
            dir_path = Path(item.path)
            for predicate in predicates:
                if predicate(dir_path):
                    results[dir_path] = True
                    break

    return results