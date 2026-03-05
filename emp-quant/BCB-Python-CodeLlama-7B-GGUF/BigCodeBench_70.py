
import pandas as pd
import json
import numpy as np

# Constants
COLUMNS = ['email', 'list']

def task_func(json_file):
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data, columns=COLUMNS)

    # Calculate sum and mean of list for each email
    df['sum'] = df['list'].apply(sum)
    df['mean'] = df['list'].apply(np.mean)

    # Plot sum and mean values for each email
    fig, ax = plt.subplots()
    ax.plot(df['email'], df['sum'], label='Sum')
    ax.plot(df['email'], df['mean'], label='Mean')
    ax.set_xlabel('Email')
    ax.set_ylabel('Sum/Mean')
    ax.legend()

    # Return DataFrame and Axes object
    return df, ax

# Print the DataFrame
print(df)

# Plot the data
ax.show()