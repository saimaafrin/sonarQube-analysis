
import os
import re
from datetime import datetime

def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.
    
    Args:
    pattern (str): The regex pattern to match against the log file names.
    log_dir (str): The directory to search for log files. Defaults to '/var/log/'.
    
    Returns:
    str or None: The path to the most recent log file that matches the pattern, or None if no matching files are found.
    """
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Initialize variables to store the most recent file and its modification time
    most_recent_file = None
    most_recent_time = None
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(log_dir):
        # Check if the file matches the regex pattern
        if regex.match(filename):
            # Construct the full file path
            file_path = os.path.join(log_dir, filename)
            # Get the modification time of the file
            mod_time = os.path.getmtime(file_path)
            # Convert the modification time to a datetime object
            mod_time_dt = datetime.fromtimestamp(mod_time)
            # Update the most recent file if this file is newer
            if most_recent_time is None or mod_time_dt > most_recent_time:
                most_recent_file = file_path
                most_recent_time = mod_time_dt
    
    return most_recent_file