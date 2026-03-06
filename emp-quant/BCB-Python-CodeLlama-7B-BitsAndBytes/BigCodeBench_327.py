
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.

    Args:
        file_path (str): Path to the CSV file.
        regex_pattern (str): Regex pattern to use for matching.

    Returns:
        dict: A dictionary with counts of matches.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        matches = []
        for row in reader:
            for cell in row:
                matches.extend(re.findall(regex_pattern, cell))
    return Counter(matches)