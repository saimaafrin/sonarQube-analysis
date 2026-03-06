
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
    # Initialize counter for goals and penalties
    count = Counter()
    
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
    
    # Read the existing data from the CSV file
    with open(csv_file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            count['goals'] += int(row['goals'])
            count['penalties'] += int(row['penalties'])
    
    # Add new goals and penalties to the counter
    count['goals'] += goals
    count['penalties'] += penalties
    
    return count