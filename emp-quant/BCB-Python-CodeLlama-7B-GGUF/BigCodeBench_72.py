
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Find the longest filename in the directory
    file_names = [f for f in os.listdir(directory) if f.endswith('.csv')]
    longest_file_name = max(file_names, key=len)

    # Load the CSV file with the longest filename
    df = pd.read_csv(os.path.join(directory, longest_file_name))

    # Convert the list column to a list
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and median of the list column
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)

    # Draw a histogram of the median
    hist, bins = np.histogram(df['median'], bins=50)
    ax = hist.plot(kind='bar')

    return df, ax