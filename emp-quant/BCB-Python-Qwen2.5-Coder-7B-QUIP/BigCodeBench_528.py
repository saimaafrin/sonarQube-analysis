
import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    # Read the CSV file using csv library
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Check if the file is empty
    if not data:
        raise ValueError("CSV file is empty")

    # Check if the file has a .csv extension
    if not file_path.endswith('.csv'):
        raise ValueError("File format is not supported. Please provide a CSV file.")

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])

    # Identify duplicate rows
    duplicate_rows = df.duplicated(subset=df.columns, keep=False)

    # Get the count of duplicate rows
    duplicate_counts = Counter(df[duplicate_rows].iloc[:, 0])

    # Create a dictionary with duplicate rows as keys and their counts as values
    duplicate_dict = dict(duplicate_counts)

    # Plot the bar chart of duplicate rows
    fig, ax = plt.subplots()
    ax.bar(duplicate_dict.keys(), duplicate_dict.values())
    ax.set_xlabel('Duplicate Rows')
    ax.set_ylabel('Count')
    ax.set_title('Duplicate Rows in CSV File')

    return duplicate_dict, ax