import pandas as pd
import json
import numpy as np
COLUMNS = ['email', 'list']
def task_func(json_file):
    # Load data from JSON file
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        return pd.DataFrame(columns=COLUMNS + ['sum', 'mean']), None

    # Convert data into a DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate sum and mean for each email
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)

    # Plot the sum and mean values
    if not df.empty:
        ax = df.plot(kind='bar', x='email', y=['sum', 'mean'], figsize=(10, 5))
    else:
        ax = None

    return df, ax