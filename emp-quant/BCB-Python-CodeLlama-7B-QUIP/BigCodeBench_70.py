
import pandas as pd
import json
import numpy as np
# Constants
COLUMNS = ['email', 'list']
def task_func(json_file):
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)
    # Create an empty dataframe with the right columns
    df = pd.DataFrame(columns=COLUMNS)
    # Loop through the data and calculate the sum and mean for each email
    for email, list in data.items():
        sum = np.sum(list)
        mean = np.mean(list)
        df = df.append({'email': email, 'list': list, 'sum': sum, 'mean': mean},
                       ignore_index=True)
    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(df['sum'], df['mean'])
    return df, ax