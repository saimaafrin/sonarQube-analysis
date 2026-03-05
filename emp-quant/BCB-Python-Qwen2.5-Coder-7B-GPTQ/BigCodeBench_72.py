import pandas as pd
import os
import numpy as np
import ast
def task_func(directory):
    # Check if the directory is empty
    if not os.listdir(directory):
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None
    
    # Find the CSV file with the longest filename
    longest_csv = max([f for f in os.listdir(directory) if f.endswith('.csv')], key=len)
    csv_path = os.path.join(directory, longest_csv)
    
    # Load the CSV file
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None
    
    # Convert the 'list' column to actual Python lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate the sum, mean, and median of the 'list' column
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)
    
    # Plot the histogram of the median
    if not df.empty:
        ax = df['median'].hist()
        return df, ax
    else:
        return df, None