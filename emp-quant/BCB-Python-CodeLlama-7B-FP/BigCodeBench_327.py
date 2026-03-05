import csv
import re
from collections import Counter
def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.
    By default, it captures content between parentheses as a single match and any word or sequence of non-alphanumeric characters outside as matches in a string.
    """
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        matches = []
        for row in reader:
            for cell in row:
                matches.extend(re.findall(regex_pattern, cell))
    return Counter(matches)
file_path = 'test_data.csv'
regex_pattern = r'\(.+?\)|\w+|[\W_]+'