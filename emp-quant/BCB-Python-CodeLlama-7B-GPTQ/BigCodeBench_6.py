import os
import re
def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.
    This function searches through all files in the specified directory, filters them based on the provided regex pattern, and returns the path to the most recent log file based on modification time. If no files match the pattern or the directory is empty, the function returns None.
    """
    # Check if the log directory exists
    if not os.path.isdir(log_dir):
        return None

    # Get a list of all files in the log directory
    files = os.listdir(log_dir)

    # Filter the list of files based on the provided regex pattern
    filtered_files = [file for file in files if re.search(pattern, file)]

    # If no files match the pattern, return None
    if not filtered_files:
        return None

    # Get the most recent file based on modification time
    most_recent_file = max(filtered_files, key=os.path.getmtime)

    # Return the path to the most recent file
    return os.path.join(log_dir, most_recent_file)