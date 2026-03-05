import csv
import os
from collections import Counter
CSV_FILE_PATH = 'match_data.csv'
def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    """
    Count the total number of goals and penalties from a CSV file and update it with the given goals and penalties.
    The function should output with:
        count (Counter.collections): A Counter object with total counts of goals and penalties.
    """
    # Open the CSV file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Create a Counter object to store the counts
        count = Counter()
        # Iterate over the rows in the CSV file
        for row in reader:
            # Increment the count for the current row
            count.update([row[1], row[2]])
        # Update the counts with the given goals and penalties
        count.update(goals)
        count.update(penalties)
    return count