
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.
    By default, it captures content between parentheses as a single match and any word or sequence of non-alphanumeric characters outside as matches in a string.
    :param file_path: Path to the CSV file.
    :param regex_pattern: Regex pattern to use for matching.
    :return: Dictionary with counts of matches.
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        matches = []
        for row in reader:
            for match in re.findall(regex_pattern, row):
                matches.append(match)
    return Counter(matches)