import csv
import re
from collections import Counter
def task_func(file_path, regex_pattern=r'\(.+?\)|\w+|[\W_]+'):
    # Initialize a Counter object to store the counts of matches
    match_counts = Counter()
    
    # Open the CSV file for reading
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Iterate over each cell in the row
            for cell in row:
                # Find all matches in the cell using the provided regex pattern
                matches = re.findall(regex_pattern, cell)
                
                # Update the match_counts dictionary with the counts of each match
                match_counts.update(matches)
    
    # Return the dictionary with counts of matches
    return dict(match_counts)
file_path = 'sample.csv'
regex_pattern = r'\(.+?\)|\w+|[\W_]+'