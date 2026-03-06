
import pathlib
import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    """
    Validates that a given file path does not contain invalid characters for file paths
    then splits it into path components using a specified delimiter.

    Args:
        path (str): The file path to validate and split.
        delimiter (str, optional): The delimiter to use when splitting the path. Defaults to os.path.sep.

    Returns:
        list: A list of the path components if the path is valid;
        otherwise, an empty list if the path contains invalid characters.

    Raises:
        ValueError: If the path contains invalid characters.
    """
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')

    # Check for invalid characters in the path
    invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
    for char in invalid_chars:
        if char in path:
            raise ValueError(f"Invalid character '{char}' in path")

    # Split the path into components using the specified delimiter
    components = path.split(delimiter)

    # Return the list of path components
    return components