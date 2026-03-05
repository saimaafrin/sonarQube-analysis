
import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    # Load data from JSON file
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS + ['sum', 'mean']), None

    # Convert data into DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate sum and mean of the list for each email
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)

    # Plot the sum and mean values for each email
    if not df.empty:
        fig, ax = plt.subplots()
        ax.bar(df['email'], df['sum'], label='Sum')
        ax.bar(df['email'], df['mean'], bottom=df['sum'], label='Mean')
        ax.set_xlabel('Email')
        ax.set_ylabel('Values')
        ax.set_title('Sum and Mean of List for Each Email')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
    else:
        fig, ax = None, None

    return df, ax