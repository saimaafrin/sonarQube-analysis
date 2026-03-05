
import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    # Check if the file has a .csv extension
    if not file_path.endswith('.csv'):
        raise ValueError("The file must be in CSV format with a .csv extension.")
    
    # Read the CSV file and store rows in a list
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
    
    # Count occurrences of each row
    row_counts = Counter(tuple(row) for row in rows)
    
    # Filter out rows that occur only once
    duplicates = {row: count for row, count in row_counts.items() if count > 1}
    
    # Convert duplicates to a pandas DataFrame
    df = pd.DataFrame(list(duplicates.keys()), columns=[f'Column_{i+1}' for i in range(len(rows[0]))])
    
    # Plotting the bar chart
    fig, ax = plt.subplots()
    ax.bar(duplicates.keys(), duplicates.values())
    ax.set_xlabel('Duplicate Rows')
    ax.set_ylabel('Count')
    ax.set_title('Duplicate Rows in CSV File')
    
    return duplicates, ax