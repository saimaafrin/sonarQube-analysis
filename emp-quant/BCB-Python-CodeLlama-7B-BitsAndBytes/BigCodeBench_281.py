
import re
import os
from collections import Counter

def task_func(folder_path: str) -> dict:
    """
    Scan a directory for log files and count the occurrences of each IP address in all files.

    Args:
        folder_path (str): The path to the directory containing the log files.

    Returns:
        dict: A dictionary with IP addresses as keys and their counts as values.
    """
    ip_address_pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    ip_address_counter = Counter()

    for root, _, files in os.walk(folder_path):
        for file in files:
            with open(os.path.join(root, file), "r") as f:
                for line in f:
                    for ip_address in re.findall(ip_address_pattern, line):
                        ip_address_counter[ip_address] += 1

    return ip_address_counter