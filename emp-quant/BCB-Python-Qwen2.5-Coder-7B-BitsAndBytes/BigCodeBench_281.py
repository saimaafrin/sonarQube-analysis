
import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    # Regular expression pattern to match IP addresses
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    
    # Dictionary to store the count of each IP address
    ip_counts = Counter()
    
    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.log'):  # Check if the file is a log file
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Find all IP addresses in the file
                    ips = ip_pattern.findall(content)
                    # Update the count of each IP address
                    ip_counts.update(ips)
    
    return dict(ip_counts)