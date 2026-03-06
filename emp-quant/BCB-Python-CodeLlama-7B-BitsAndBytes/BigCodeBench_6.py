
import os
import re

def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.

    Args:
        pattern (str): The regex pattern to match against.
        log_dir (str, optional): The directory to search for log files. Defaults to '/var/log/'.

    Returns:
        str or None: The path to the most recent log file that matches the pattern, or None if no matching files are found.
    """
    # Get a list of all files in the log directory
    files = os.listdir(log_dir)

    # Filter the list to only include files that match the pattern
    filtered_files = [file for file in files if re.search(pattern, file)]

    # If no files match the pattern, return None
    if not filtered_files:
        return None

    # Get the most recent file based on modification time
    most_recent_file = max(filtered_files, key=os.path.getmtime)

    # Return the path to the most recent file
    return os.path.join(log_dir, most_recent_file)