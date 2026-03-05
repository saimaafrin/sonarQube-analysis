
import pathlib
import os

def task_func(path: str, delimiter: str = os.path.sep) -> list:
    """
    Validates that a given file path does not contain invalid characters for file paths then splits it into path components using a specified delimiter.

    Args:
        path (str): The file path to validate and split.
        delimiter (str, optional): The delimiter to use for splitting the path. Defaults to os.path.sep.

    Returns:
        list: A list of the path components if the path is valid; otherwise, an empty list if the path contains invalid characters.

    Raises:
        ValueError: If the path contains invalid characters.
    """
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')

    # Check for invalid characters
    if any(c in path for c in '<>:"|?*'):
        raise ValueError(f"Invalid character in path: {path}")

    # Split the path using the specified delimiter
    return path.split(delimiter)