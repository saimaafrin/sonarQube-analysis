
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.
    
    Parameters:
    - file_path: str, the path to the CSV file.
    - regex_pattern: str, the regex pattern to use for matching. Defaults to capturing content between parentheses, words, and sequences of non-alphanumeric characters.
    
    Returns:
    - dict: A dictionary with counts of matches.
    """
    # Initialize a Counter object to store the counts
    match_counts = Counter()
    
    # Open the CSV file and read its contents
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Iterate over each cell in the row
            for cell in row:
                # Find all matches in the cell using the regex pattern
                matches = re.findall(regex_pattern, cell)
                # Update the match counts
                match_counts.update(matches)
    
    # Return the dictionary of match counts
    return dict(match_counts)