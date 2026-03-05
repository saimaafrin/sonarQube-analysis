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
    # Initialize a counter to store the counts of matches
    match_counter = Counter()
    
    # Compile the regex pattern for better performance
    pattern = re.compile(regex_pattern)
    
    # Open the CSV file and read its contents
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Iterate over each cell in the row
            for cell in row:
                # Find all matches in the cell
                matches = pattern.findall(cell)
                
                # Update the counter with the matches
                match_counter.update(matches)
    
    # Return the dictionary with counts of matches
    return dict(match_counter)