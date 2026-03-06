import pandas as pd
import json
import numpy as np
def task_func(json_file):
    """
    Load e-mail data from a JSON file, convert it into a Pandas DataFrame, calculate the sum and mean
    of the list associated with each e-mail, and then record those values. Additionally, it plots the sum
    and mean values for each email.

    If there is no e-mail data, return an empty dataframe with the right columns (['email', 'list', 'sum', 'mean']), and None as the plot.

    Parameters:
    json_file (str): The path to the JSON file. The JSON file should have the structure:
                     [
                         {"email": "email1@example.com", "list": [value1, value2, ...]},
                         ...
                     ]

    Returns:
    tuple: A tuple containing:
        - DataFrame: A pandas DataFrame with columns ['email', 'list', 'sum', 'mean'].
        - Axes: The Axes object for the plot. None if the dataframe is empty.

    Requirements:
    - pandas
    - json
    - numpy

    Example:
    >>> df, ax = task_func('data/task_func/json_1.json')
    >>> print(df)
    """
    # Load the JSON file
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Convert the JSON data into a DataFrame
    df = pd.DataFrame(data)

    # Calculate the sum and mean of the list associated with each e-mail
    df['sum'] = df['list'].apply(lambda x: sum(x))
    df['mean'] = df['list'].apply(lambda x: np.mean(x))

    # Plot the sum and mean values for each email
    fig, ax = plt.subplots()
    ax.plot(df['email'], df['sum'], 'o')
    ax.plot(df['email'], df['mean'], 'o')
    ax.set_xlabel('Email')
    ax.set_ylabel('Sum/Mean')
    ax.set_title('Sum and Mean of Lists')

    # Return the DataFrame and the Axes object
    return df, ax