
import pandas as pd
import json
import numpy as np
# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    # Load data from JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over the data and calculate the sum and mean of the list
    for email, list_data in data.items():
        results.append([email, list_data, np.sum(list_data), np.mean(list_data)])
    
    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=COLUMNS + ['sum', 'mean'])
    
    # Plot the sum and mean values
    if not df.empty:
        fig, ax = plt.subplots()
        ax.plot(df['sum'], label='Sum')
        ax.plot(df['mean'], label='Mean')
        ax.set_xlabel('Email')
        ax.set_ylabel('Value')
        ax.set_title('Sum and Mean of Lists')
        ax.legend()
    else:
        fig, ax = (None, None)
    
    return df, ax