
import csv
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

def task_func(file_path):
    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Create a dictionary with duplicate rows as keys and their counts as values
    duplicates = Counter(data)

    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(duplicates, orient='index')

    # Plot the bar chart of duplicate rows
    ax = df.plot(kind='bar', title='Duplicate Rows')

    # Return the dictionary and the Axes object
    return duplicates, ax