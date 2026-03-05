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
    # Compile the regex pattern for efficiency
    regex = re.compile(pattern)
    
    # Initialize variables to store the latest log file and its modification time
    latest_log = None
    latest_time = 0
    
    # Iterate over all files in the specified directory
    for filename in os.listdir(log_dir):
        # Construct the full file path
        file_path = os.path.join(log_dir, filename)
        
        # Check if the file is a log file and matches the regex pattern
        if os.path.isfile(file_path) and regex.match(filename):
            # Get the modification time of the file
            file_time = os.path.getmtime(file_path)
            
            # Update the latest log file if the current file is newer
            if file_time > latest_time:
                latest_log = file_path
                latest_time = file_time
    
    # Return the path to the latest log file that matches the pattern
    return latest_log