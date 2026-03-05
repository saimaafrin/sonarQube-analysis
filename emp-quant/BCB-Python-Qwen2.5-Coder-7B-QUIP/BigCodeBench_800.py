
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
    # Read the existing CSV file
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found at {csv_file_path}")

    with open(csv_file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = list(reader)

    # Update the goals and penalties
    for row in data:
        if row[0] == 'Team A':
            row[1] = str(int(row[1]) + goals)
            row[2] = str(int(row[2]) + penalties)
        elif row[0] == 'Team B':
            row[1] = str(int(row[1]) + goals)
            row[2] = str(int(row[2]) + penalties)
        elif row[0] == 'Team C':
            row[1] = str(int(row[1]) + goals)
            row[2] = str(int(row[2]) + penalties)

    # Write the updated data back to the CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    # Count the total number of goals and penalties
    with open(csv_file_path, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        counts = Counter()
        for row in reader:
            counts['goals'] += int(row[1])
            counts['penalties'] += int(row[2])

    return counts