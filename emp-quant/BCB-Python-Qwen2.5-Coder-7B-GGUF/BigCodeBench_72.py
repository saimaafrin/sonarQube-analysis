
import pandas as pd
import os
import numpy as np
import ast
import matplotlib.pyplot as plt

def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    # Find the CSV file with the longest filename
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    if not csv_files:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    longest_csv = max(csv_files, key=len)
    csv_path = os.path.join(directory, longest_csv)

    # Load the CSV file
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None

    # Convert the 'list' column from string to actual list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate sum, mean, and median
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Plot the histogram of the median
    if not df.empty:
        plt.figure(figsize=(10, 6))
        plt.hist(df['median'], bins=20, color='blue', edgecolor='black')
        plt.title('Histogram of Median')
        plt.xlabel('Median')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        plt = None

    return df, plt