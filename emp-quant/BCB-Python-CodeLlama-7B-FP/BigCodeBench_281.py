import re
import os
from collections import Counter
def task_func(folder_path: str) -> dict:
    """
    Scan a directory for log files and count the occurrences of each IP address in all files.
    The function utilizes a regular expression pattern to identify IP addresses in the log files.
    The function should output with:
        dict: A dictionary with IP addresses as keys and their counts as values.
    """
    ip_address_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
    ip_address_counts = Counter()

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".log"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        for ip_address in ip_address_pattern.findall(line):
                            ip_address_counts[ip_address] += 1

    return ip_address_counts
folder_path = "./logs"