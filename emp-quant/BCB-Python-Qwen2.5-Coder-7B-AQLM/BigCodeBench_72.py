
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    # Initialize variables to store the longest filename and its corresponding DataFrame
    longest_filename = None
    longest_df = pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median'])

    # Traverse the directory for CSV files
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            # Load the CSV file into a DataFrame
            df = pd.read_csv(file_path)
            # Convert the 'list' column from string to actual list
            df['list'] = df['list'].apply(ast.literal_eval)
            # Calculate the sum, mean, and median of the 'list' column
            df['sum'] = df['list'].apply(sum)
            df['mean'] = df['list'].apply(np.mean)
            df['median'] = df['list'].apply(np.median)
            # Update the longest filename and DataFrame if the current one has a longer filename
            if longest_filename is None or len(filename) > len(longest_filename):
                longest_filename = filename
                longest_df = df

    # Return the DataFrame with the longest filename and its histogram of the median
    if longest_df.empty:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None
    else:
        return longest_df, longest_df['median'].hist(bins=10)