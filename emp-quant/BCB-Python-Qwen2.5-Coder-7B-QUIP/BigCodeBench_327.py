
import csv
import re
from collections import Counter

def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    # Initialize a Counter to store the counts of matches
    match_counts = Counter()
    
    # Open the CSV file and read through it
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Use regex to find matches in each row
            matches = re.findall(regex_pattern, ''.join(row))
            # Update the count for each match
            match_counts.update(matches)
    
    # Return the dictionary of match counts
    return dict(match_counts)