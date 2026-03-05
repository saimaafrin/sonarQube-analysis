import csv
import re
from collections import Counter
def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    """
    Counts matches from a CSV file based on a given regex pattern.
    
    Args:
    file_path (str): The path to the CSV file.
    regex_pattern (str): The regex pattern to use for matching. Defaults to capturing content between parentheses, words, and sequences of non-alphanumeric characters.
    
    Returns:
    dict: A dictionary with counts of matches.
    """
    # Initialize a counter to store the counts of matches
    match_counter = Counter()
    
    # Open the CSV file and read its contents
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Iterate over each cell in the row
            for cell in row:
                # Find all matches in the cell using the regex pattern
                matches = re.findall(regex_pattern, cell)
                
                # Update the counter with the matches
                match_counter.update(matches)
    
    # Return the dictionary with counts of matches
    return dict(match_counter)