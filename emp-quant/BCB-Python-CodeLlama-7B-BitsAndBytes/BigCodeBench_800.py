
import csv
import os
from collections import Counter

# Constants
CSV_FILE_PATH = 'match_data.csv'

# Create a test CSV file
def create_test_csv(filename, content):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(content)

# Function to count the total number of goals and penalties from a CSV file
def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    # Open the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Create a Counter object to store the counts
        counts = Counter()
        # Iterate over the rows in the CSV file
        for row in reader:
            # Increment the counts for the goals and penalties
            counts['goals'] += int(row[1])
            counts['penalties'] += int(row[2])
        # Return the Counter object
        return counts

# Run the tests