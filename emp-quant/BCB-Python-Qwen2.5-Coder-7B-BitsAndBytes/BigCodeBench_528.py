
import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    # Check if the file path ends with .csv
    if not file_path.endswith('.csv'):
        raise ValueError("File must be in CSV format.")
    
    # Read the CSV file
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    
    # Convert list of dictionaries to pandas DataFrame
    df = pd.DataFrame(data)
    
    # Identify duplicate rows
    duplicates = df.duplicated(keep=False)
    duplicate_rows = df[duplicates].reset_index(drop=True)
    
    # Count occurrences of each duplicate row
    duplicate_counts = Counter(tuple(row) for _, row in duplicate_rows.iterrows())
    
    # Create a dictionary with duplicate rows as keys and their counts as values
    duplicate_dict = {tuple(row): count for row, count in duplicate_counts.items()}
    
    # Plotting
    fig, ax = plt.subplots()
    ax.bar(duplicate_dict.keys(), duplicate_dict.values(), color='blue')
    ax.set_xlabel('Duplicate Rows')
    ax.set_ylabel('Count')
    ax.set_title('Duplicate Rows in CSV File')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return duplicate_dict, ax