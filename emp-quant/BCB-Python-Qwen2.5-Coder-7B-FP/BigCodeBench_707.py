import json
import numpy as np
import pandas as pd
def task_func(df):
    """
    Transforms the 'IntCol' column of the given DataFrame by applying a logarithm (base 10)
    and writes the transformed column to a 'IntCol.json' file as a list.
    
    Parameters:
    df (DataFrame): A pandas DataFrame with an 'IntCol' column.
    
    Returns:
    df (DataFrame): The original DataFrame with the 'IntCol' column transformed.
    """
    # Apply logarithm base 10 to the 'IntCol' column
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the transformed column to a list
    transformed_list = df['IntCol'].tolist()
    
    # Write the list to a JSON file
    with open('IntCol.json', 'w') as json_file:
        json.dump(transformed_list, json_file)
    
    return df