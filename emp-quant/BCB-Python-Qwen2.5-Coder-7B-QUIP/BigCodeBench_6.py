
import os
import re
def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.
    
    :param pattern: str, the regex pattern to match the log files.
    :param log_dir: str, the directory to search for log files.
    :return: str or None, the path to the most recent log file that matches the pattern, or None if no matching files are found.
    """
    # List all files in the directory
    files = os.listdir(log_dir)
    
    # Filter files based on the regex pattern
    matching_files = [file for file in files if re.match(pattern, file)]
    
    # If no matching files, return None
    if not matching_files:
        return None
    
    # Find the most recent log file
    latest_file = max(matching_files, key=lambda x: os.path.getmtime(os.path.join(log_dir, x)))
    
    # Return the path to the most recent log file
    return os.path.join(log_dir, latest_file)