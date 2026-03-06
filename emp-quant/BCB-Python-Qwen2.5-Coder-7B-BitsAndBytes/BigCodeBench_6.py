
import os
import re

def task_func(pattern, log_dir='/var/log/'):
    """
    Find the latest log file in a specified directory that matches a given regex pattern.

    Args:
        pattern (str): The regex pattern to filter log files.
        log_dir (str): The directory to search for log files. Defaults to '/var/log/'.

    Returns:
        str or None: The path to the most recent log file that matches the pattern, or None if no matching files are found.
    """
    # Compile the regex pattern for efficient matching
    compiled_pattern = re.compile(pattern)
    
    # Initialize variables to store the latest log file and its modification time
    latest_log_file = None
    latest_mod_time = 0
    
    # List all files in the specified directory
    for filename in os.listdir(log_dir):
        # Construct full file path
        file_path = os.path.join(log_dir, filename)
        
        # Check if it's a file and matches the regex pattern
        if os.path.isfile(file_path) and compiled_pattern.match(filename):
            # Get the last modified time of the file
            mod_time = os.path.getmtime(file_path)
            
            # Update the latest log file if this one is newer
            if mod_time > latest_mod_time:
                latest_log_file = file_path
                latest_mod_time = mod_time
    
    return latest_log_file