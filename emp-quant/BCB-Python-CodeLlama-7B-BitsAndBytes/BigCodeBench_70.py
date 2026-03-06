
import pandas as pd
import json
import numpy as np
# Constants
COLUMNS = ['email', 'list']
def task_func(json_file):
    # Load the JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Create an empty DataFrame with the right columns
    df = pd.DataFrame(columns=COLUMNS)

    # Iterate over the data and calculate the sum and mean of the list associated with each email
    for email, email_data in data.items():
        list_data = email_data['list']
        sum_val = np.sum(list_data)
        mean_val = np.mean(list_data)
        df = df.append({'email': email, 'list': list_data, 'sum': sum_val, 'mean': mean_val}, ignore_index=True)

    # Plot the sum and mean values for each email
    if not df.empty:
        fig, ax = plt.subplots()
        ax.plot(df['email'], df['sum'], label='Sum')
        ax.plot(df['email'], df['mean'], label='Mean')
        ax.set_xlabel('Email')
        ax.set_ylabel('Sum and Mean')
        ax.legend()
        return df, ax
    else:
        return df, None

# Call the function and pass the JSON file as an argument
df, ax = task_func('data.json')
print(df)