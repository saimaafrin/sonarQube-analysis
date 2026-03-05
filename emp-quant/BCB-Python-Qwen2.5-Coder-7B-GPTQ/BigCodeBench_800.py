import csv
import os
from collections import Counter
CSV_FILE_PATH = 'match_data.csv'
def task_func(goals, penalties, csv_file_path=CSV_FILE_PATH):
    count = Counter()
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            count['goals'] += int(row[1])
            count['penalties'] += int(row[2])
    count['goals'] += goals
    count['penalties'] += penalties
    return count