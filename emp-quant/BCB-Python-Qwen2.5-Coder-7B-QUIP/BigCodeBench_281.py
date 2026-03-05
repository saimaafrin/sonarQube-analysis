
import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    # Define the regular expression pattern for IP addresses
    ip_pattern = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b')

    # Initialize a Counter to store the counts of each IP address
    ip_counts = Counter()

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a log file
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                # Read the contents of the log file
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Find all IP addresses in the content
                    ip_addresses = ip_pattern.findall(content)
                    # Update the count for each IP address
                    ip_counts.update(ip_addresses)

    # Return the dictionary with IP addresses and their counts
    return dict(ip_counts)