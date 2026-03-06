
import pandas as pd
import os
import numpy as np
import ast

def task_func(directory):
    # Check if the directory exists
    if not os.path.exists(directory):
        return pd.DataFrame(), None
    
    # Initialize variables
    max_length = 0
    selected_file = None
    
    # Traverse the directory for CSV files
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            if len(filename) > max_length:
                max_length = len(filename)
                selected_file = os.path.join(directory, filename)
    
    # Load the CSV file with the longest filename
    if selected_file:
        df = pd.read_csv(selected_file)
        
        # Convert the string representation of lists to actual lists
        df['list'] = df['list'].apply(ast.literal_eval)
        
        # Calculate sum, mean, and median
        df['sum'] = df['list'].apply(sum)
        df['mean'] = df['list'].apply(np.mean)
        df['median'] = df['list'].apply(np.median)
        
        # Draw a histogram of the median
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        df['median'].hist(ax=ax)
        plt.title('Histogram of Median')
        plt.xlabel('Median')
        plt.ylabel('Frequency')
        plt.show()
        
        return df, ax
    else:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None