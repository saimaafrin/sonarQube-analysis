
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.

    Args:
        file_path (str): The path to the CSV file.
        regex_pattern (str): The regex pattern to use for matching.

    Returns:
        dict: A dictionary with counts of matches.
    """
    # Initialize a counter to store the matches
    match_counter = Counter()

    # Open the CSV file and read its contents
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Join all elements in the row into a single string
            row_string = ' '.join(row)
            
            # Find all matches using the provided regex pattern
            matches = re.findall(regex_pattern, row_string)
            
            # Update the counter with the found matches
            match_counter.update(matches)

    return dict(match_counter)