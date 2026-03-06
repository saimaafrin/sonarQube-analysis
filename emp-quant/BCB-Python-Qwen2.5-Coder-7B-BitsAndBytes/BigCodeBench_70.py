
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
    
    # Convert to DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)
    
    # Calculate sum and mean
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)
    
    # Plotting
    if not df.empty:
        fig, ax = plt.subplots()
        ax.plot(df['email'], df['sum'], label='Sum')
        ax.plot(df['email'], df['mean'], label='Mean')
        ax.set_xlabel('Email')
        ax.set_ylabel('Values')
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        return df, ax
    else:
        return df, None