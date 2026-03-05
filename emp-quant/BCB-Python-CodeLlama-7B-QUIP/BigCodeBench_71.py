
import pandas as pd
import seaborn as sns
import numpy as np
import ast

def task_func(csv_file):
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Convert the email column to a list
    df['list'] = df['email'].apply(ast.literal_eval)

    # Calculate the sum, mean, and standard deviation of the list
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)

    # Draw a histogram of the mean values
    fig, ax = plt.subplots()
    ax.hist(df['mean'])

    # Return the DataFrame and the histogram plot
    return df, fig