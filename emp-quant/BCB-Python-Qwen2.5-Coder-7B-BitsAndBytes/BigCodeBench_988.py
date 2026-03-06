
import os
import re
from pathlib import Path

def task_func(dir_path: str, predicates: list) -> dict:
    if not predicates:
        raise ValueError("No valid predicates provided.")
    
    dir_path = Path(dir_path)
    if not dir_path.is_dir():
        raise FileNotFoundError(f"The specified path '{dir_path}' does not exist or is not a directory.")
    
    results = {}
    for item in dir_path.iterdir():
        item_name = item.name
        result = any(predicate(item_name) for predicate in predicates)
        results[item_name] = result
    
    return results