
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Check if there are any CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not csv_files:
        return pd.DataFrame(), None

    # Find the CSV file with the longest filename
    longest_csv = max(csv_files, key=len)

    # Load the CSV file into a DataFrame
    df = pd.read_csv(os.path.join(directory, longest_csv))

    # Convert the 'list' column from string to list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Draw a histogram of the median
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.hist(df['median'], bins=30)
    ax.set_xlabel('Median')
    ax.set_ylabel('Frequency')

    return df, ax