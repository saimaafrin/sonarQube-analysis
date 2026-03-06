
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Find the longest filename in the directory
    longest_filename = None
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            if longest_filename is None or len(filename) > len(longest_filename):
                longest_filename = filename

    # Load the CSV file with the longest filename
    if longest_filename is not None:
        df = pd.read_csv(os.path.join(directory, longest_filename))

        # Convert the 'list' column to a list
        df['list'] = df['list'].apply(ast.literal_eval)

        # Calculate the sum, mean, and median of the 'list' column
        sum_list = df['list'].sum()
        mean_list = df['list'].mean()
        median_list = df['list'].median()

        # Create a histogram of the median
        hist, bins = np.histogram(median_list, bins=20)
        ax = plt.axes()
        ax.hist(bins, hist, cumulative=True, label='Cumulative Histogram')
        ax.set_xlabel('Median')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of Median')
        ax.legend()

        # Return the DataFrame with the calculated columns
        return df[['email', 'list', 'sum', 'mean', 'median']]
    else:
        # Return an empty DataFrame with the expected columns
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median'])