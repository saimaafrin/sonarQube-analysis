
import csv
import os
from collections import Counter

# Constants
CSV_FILE_PATH = 'match_data.csv'

def create_test_csv(filename, content):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(content)

def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    # Open the CSV file in read mode
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Create a Counter object to keep track of the total counts of goals and penalties
        counter = Counter()
        for row in reader:
            # Check if the row is a header row
            if row[0] == 'team':
                # If it is, skip it
                continue
            # Add the goals and penalties to the Counter object
            counter.update([row[1], row[2]])
    # Update the CSV file with the given goals and penalties
    with open(csv_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows([['team', 'goals', 'penalties']])
        writer.writerows(goals, penalties)
    return counter