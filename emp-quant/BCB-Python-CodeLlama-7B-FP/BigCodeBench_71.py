import pandas as pd
import seaborn as sns
import numpy as np
import ast
def task_func(csv_file):
    # Load e-mail data from a CSV file
    df = pd.read_csv(csv_file)

    # Convert the list column to a list of integers
    df['list'] = df['list'].apply(ast.literal_eval)

    # Calculate the sum, mean, and standard deviation of the list associated with each e-mail
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    df['std'] = df['list'].apply(np.std)

    # Draw a histogram of the mean values
    sns.histplot(df['mean'], bins=20)

    # Return the DataFrame and the histogram plot
    return df, sns.histplot(df['mean'], bins=20)