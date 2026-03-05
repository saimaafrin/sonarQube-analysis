import csv
import os
from collections import Counter
CSV_FILE_PATH = 'match_data.csv'
def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    # Initialize a Counter object to store the total counts of goals and penalties
    count = Counter()
    
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
    
    # Read the CSV file and update the Counter object
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            count['goals'] += int(row['goals'])
            count['penalties'] += int(row['penalties'])
    
    # Add the given goals and penalties to the Counter object
    count['goals'] += goals
    count['penalties'] += penalties
    
    return count