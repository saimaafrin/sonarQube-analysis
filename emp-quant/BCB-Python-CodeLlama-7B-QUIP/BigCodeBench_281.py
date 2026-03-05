
import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    ip_counts = Counter()
    for file_name in os.listdir(folder_path):
        with open(os.path.join(folder_path, file_name), "r") as f:
            for line in f:
                ip_match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                if ip_match:
                    ip_counts[ip_match.group(0)] += 1
    return ip_counts