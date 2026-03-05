import csv
import os
from collections import Counter
CSV_FILE_PATH = 'match_data.csv'
def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    """
    Count the total number of goals and penalties from a CSV file and update it with the given goals and penalties.
    :param goals: A list of goals to be added to the CSV file
    :param penalties: A list of penalties to be added to the CSV file
    :param csv_file_path: The path to the CSV file
    :return: A Counter object with total counts of goals and penalties
    """
    # Open the CSV file
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Create a Counter object to keep track of the total number of goals and penalties
        counter = Counter()
        # Iterate over the rows in the CSV file
        for row in reader:
            # Increment the counter for each goal and penalty
            counter['goals'] += int(row[1])
            counter['penalties'] += int(row[2])
        # Add the given goals and penalties to the counter
        counter['goals'] += sum(goals)
        counter['penalties'] += sum(penalties)
        # Return the counter
        return counter