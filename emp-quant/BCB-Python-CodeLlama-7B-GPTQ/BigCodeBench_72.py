import pandas as pd
import os
import numpy as np
import ast
def task_func(directory):
    # Traverse the directory for CSV files
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Get the file with the longest filename
    longest_file = max(csv_files, key=len)

    # Load the data from the CSV file
    df = pd.read_csv(os.path.join(directory, longest_file))

    # Convert the list column to a list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list column
    df['sum'] = df['list'].sum()
    df['mean'] = df['list'].mean()
    df['median'] = df['list'].median()

    # Draw a histogram of the median
    hist = df['median'].hist(bins=10)

    # Return the DataFrame and histogram
    return df, hist
directory = 'path/to/directory'