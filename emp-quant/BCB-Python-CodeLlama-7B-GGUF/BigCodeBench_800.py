
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
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Skip the header row
        next(reader)
        # Create a Counter object to keep track of goals and penalties
        counts = Counter()
        # Iterate over the rows in the CSV file
        for row in reader:
            # Increment the counts for goals and penalties
            counts['goals'] += int(row[1])
            counts['penalties'] += int(row[2])
        # Add the given goals and penalties to the counts
        counts['goals'] += goals
        counts['penalties'] += penalties
        # Return the Counter object
        return counts

# Run the tests
test_task_func()