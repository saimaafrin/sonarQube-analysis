
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.
    
    Parameters:
    - file_path: str, the path to the CSV file.
    - regex_pattern: str, the regex pattern to match. Defaults to capturing content between parentheses,
      words, and sequences of non-alphanumeric characters.
    
    Returns:
    - dict: A dictionary with counts of matches.
    """
    match_counts = Counter()
    
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                matches = re.findall(regex_pattern, item)
                match_counts.update(matches)
    
    return dict(match_counts)