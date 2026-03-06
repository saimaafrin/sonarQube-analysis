import re
import os
from collections import Counter
def task_func(folder_path: str) -> dict:
    """
    Scan a directory for log files and count the occurrences of each IP address in all files.
    
    Parameters:
    - folder_path (str): The path to the directory containing log files to be scanned.
    
    Returns:
    dict: A dictionary with IP addresses as keys and their counts as values.
    
    Requirements:
    - re
    - os
    - collections.Counter
    
    The function utilizes a regular expression pattern to identify IP addresses in the log files.
    
    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp() # Create a temporary directory that is empty
    >>> task_func(temp_dir)
    {}
    """
    # Create a regular expression pattern to identify IP addresses in the log files
    pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    # Create an empty dictionary to store the IP addresses and their counts
    ip_counts = {}
    # Iterate over all files in the directory
    for file_name in os.listdir(folder_path):
        # Open the file and read its contents
        with open(os.path.join(folder_path, file_name), "r") as file:
            file_contents = file.read()
        # Iterate over all IP addresses in the file
        for ip_address in pattern.findall(file_contents):
            # Increment the count of the IP address in the dictionary
            ip_counts[ip_address] = ip_counts.get(ip_address, 0) + 1
    # Return the dictionary with IP addresses and their counts
    return ip_counts