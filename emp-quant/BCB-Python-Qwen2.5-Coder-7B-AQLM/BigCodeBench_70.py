
import pandas as pd
import json
import numpy as np
# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    # Load data from JSON file
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS + ['sum', 'mean']), None

    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate sum and mean for each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)

    # Plot the sum and mean values
    if not df.empty:
        ax = df.plot(kind='bar', x='email', y=['sum', 'mean'], figsize=(10, 6))
        ax.set_title('Sum and Mean of List for Each Email')
        ax.set_xlabel('Email')
        ax.set_ylabel('Values')
        ax.legend(title='Values')
    else:
        ax = None

    return df, ax