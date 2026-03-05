import pandas as pd
import json
import numpy as np
COLUMNS = ['email', 'list']
def task_func(json_file):
    # Load e-mail data from a JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Convert it into a Pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate the sum and mean of the list associated with each e-mail
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)

    # Record those values
    df = df[['email', 'list', 'sum', 'mean']]

    # Plot the sum and mean values for each email
    if not df.empty:
        fig, ax = plt.subplots()
        ax.plot(df['sum'], label='Sum')
        ax.plot(df['mean'], label='Mean')
        ax.legend()
        return df, ax
    else:
        return pd.DataFrame(columns=COLUMNS), None