
import os
import re

def task_func(pattern, log_dir='/var/log/'):
    # Create a list of all files in the log directory
    files = os.listdir(log_dir)

    # Filter the list to only include files that match the regex pattern
    files = [f for f in files if re.match(pattern, f)]

    # Sort the list by modification time, descending
    files.sort(key=os.path.getmtime, reverse=True)

    # Return the first element of the list, which is the most recent file
    if files:
        return files[0]
    else:
        return None