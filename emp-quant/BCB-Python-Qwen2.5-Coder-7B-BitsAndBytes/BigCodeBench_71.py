
import pandas as pd
import seaborn as sns
import numpy as np
import ast

def task_func(csv_file):
    # Load email data from CSV file
    df = pd.read_csv(csv_file)
    
    # Convert the string representation of lists to actual lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and standard deviation for each list
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)
    
    # Draw a histogram of the mean values
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(df['mean'], bins=30, kde=True)
    plt.title('Histogram of Mean Values')
    plt.xlabel('Mean Value')
    plt.ylabel('Frequency')
    
    # Return the DataFrame and the histogram plot
    return (df[['email', 'list', 'sum', 'mean', 'std']], ax)