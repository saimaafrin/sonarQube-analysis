import pandas as pd
import os
import numpy as np
import ast
def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    # Initialize variables
    longest_file = None
    max_length = 0

    # Traverse the directory for CSV files
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            if len(filename) > max_length:
                longest_file = filename
                max_length = len(filename)

    # If no CSV file is found, return an empty DataFrame and None
    if longest_file is None:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    # Load the CSV file with the longest filename
    file_path = os.path.join(directory, longest_file)
    df = pd.read_csv(file_path)

    # Convert the 'list' column from string to actual list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list associated with each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Draw a histogram of the median
    import matplotlib.pyplot as plt
    median_values = df['median']
    if not median_values.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(median_values, bins=30, color='blue', edgecolor='black')
        plt.title('Histogram of Median Values')
        plt.xlabel('Median')
        plt.ylabel('Frequency')
        plt.show()
    else:
        plt = None

    return df, plt