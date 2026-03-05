import os
import re
def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.
    This function searches through all files in the specified directory, filters them based on the provided regex pattern, and returns the path to the most recent log file based on modification time. If no files match the pattern or the directory is empty, the function returns None.
    :param pattern: The regex pattern to match against.
    :param log_dir: The directory to search for log files.
    :return: str or None: The path to the most recent log file that matches the pattern, or None if no matching files are found.
    """
    # Create a list of all files in the log directory
    files = os.listdir(log_dir)

    # Filter the list to only include files that match the pattern
    files = [file for file in files if re.search(pattern, file)]

    # Sort the list of files by modification time, with the most recent first
    files.sort(key=os.path.getmtime, reverse=True)

    # Return the path to the first file in the list, or None if the list is empty
    if files:
        return os.path.join(log_dir, files[0])
    else:
        return None
pattern = r'^.*\.log$'
log_dir = '/var/log/'