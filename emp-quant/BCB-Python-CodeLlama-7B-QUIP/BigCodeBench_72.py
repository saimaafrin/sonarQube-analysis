
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Get the list of CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]

    # Get the longest filename
    longest_filename = max(csv_files, key=len)

    # Load the CSV file with the longest filename
    df = pd.read_csv(os.path.join(directory, longest_filename))

    # Convert the list column to a list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list column
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Plot the histogram of the median
    fig, ax = plt.subplots()
    ax.hist(df['median'])

    return df, ax