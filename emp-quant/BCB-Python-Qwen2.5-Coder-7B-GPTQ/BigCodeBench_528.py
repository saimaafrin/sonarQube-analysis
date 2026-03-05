import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
def task_func(file_path):
    # Check if the file has a .csv extension
    if not file_path.endswith('.csv'):
        raise ValueError("The file must be in .csv format.")

    # Read the CSV file and store rows in a list
    rows = []
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    # Count occurrences of each row
    row_counts = Counter(tuple(row) for row in rows)

    # Identify duplicate rows
    duplicates = {row: count for row, count in row_counts.items() if count > 1}

    # Convert duplicated rows into a pandas DataFrame
    df = pd.DataFrame(list(duplicates.keys()), columns=rows[0])

    # Plot the bar chart of duplicate rows
    fig, ax = plt.subplots()
    ax.bar(duplicates.keys(), duplicates.values())
    ax.set_xlabel('Duplicate Rows')
    ax.set_ylabel('Count')
    ax.set_title('Duplicate Rows in CSV File')

    return duplicates, ax