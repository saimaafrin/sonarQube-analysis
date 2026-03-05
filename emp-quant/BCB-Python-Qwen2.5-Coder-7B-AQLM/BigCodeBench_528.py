
import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    if not file_path.endswith('.csv'):
        raise ValueError("File must be in CSV format.")
    
    # Read the CSV file and store rows in a list
    rows = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)
    
    # Count occurrences of each row
    row_counts = Counter(rows)
    
    # Filter out rows that appear only once
    duplicates = {row: count for row, count in row_counts.items() if count > 1}
    
    # Convert duplicates to a pandas DataFrame
    df = pd.DataFrame(list(duplicates.items()), columns=['Row', 'Count'])
    
    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(df['Row'], df['Count'], color='blue')
    ax.set_xlabel('Duplicate Rows')
    ax.set_ylabel('Count')
    ax.set_title('Duplicate Rows in CSV File')
    
    return duplicates, ax