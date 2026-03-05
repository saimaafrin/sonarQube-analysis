
import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    ip_counts = Counter()
    
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.log'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    ip_addresses = ip_pattern.findall(content)
                    ip_counts.update(ip_addresses)
    
    return dict(ip_counts)