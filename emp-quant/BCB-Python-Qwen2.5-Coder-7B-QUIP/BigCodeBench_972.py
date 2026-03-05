
import pathlib
import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    # Define a set of invalid characters
    invalid_chars = {'<', '>', ':', '"', '|', '?', '*'}
    
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')
    
    # Check for invalid characters in the path
    if any(char in invalid_chars for char in path):
        raise ValueError("Invalid characters found in the path.")
    
    # Split the path using the specified delimiter
    path_components = path.split(delimiter)
    
    return path_components