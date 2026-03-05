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
    df['sum'] = df['list'].sum()
    df['mean'] = df['list'].mean()

    # Record those values
    df = df.drop(columns=['list'])

    # Plot the sum and mean values for each email
    fig, ax = plt.subplots()
    ax.plot(df['email'], df['sum'], label='Sum')
    ax.plot(df['email'], df['mean'], label='Mean')
    ax.set_xlabel('Email')
    ax.set_ylabel('Sum and Mean')
    ax.legend()

    # Return a tuple containing the DataFrame and the Axes object
    return df, ax