import pathlib
import os
def task_func(path: str, delimiter: str = os.path.sep) -> list:
    """
    Validates that a given file path does not contain invalid characters for file paths then splits it into path components using a specified delimiter.
    Notes:
        - Backslashes ('\\') are internally converted to forward slashes ('/') before processing.
        - This function treats '<', '>', ':', '"', '|', '?', '*' as invalid characters in paths.
        - The function should raise the exception for: ValueError: If the path contains invalid characters.
        - The function should output with:
            - list: A list of the path components if the path is valid;
            - otherwise, an empty list if the path contains invalid characters.
    """
    # Convert backslashes to forward slashes
    path = path.replace('\\', '/')

    # Check for invalid characters
    invalid_chars = ['<', '>', ':', '"', '|', '?', '*']
    for char in invalid_chars:
        if char in path:
            raise ValueError(f"Invalid character '{char}' in path")

    # Split the path into components using the specified delimiter
    components = path.split(delimiter)

    # Return the list of path components
    return components
path = "path/to/file.txt"