import json
import numpy as np
import pandas as pd
def task_func(df):
    """
    Transforms the 'IntCol' column of the given DataFrame by applying a logarithm (base 10) and writes it to a 'IntCol.json' file as a list.
    
    Parameters:
    df (DataFrame): A pandas DataFrame with an 'IntCol' column.
    
    Returns:
    df (DataFrame): The transformed DataFrame with the 'IntCol' column.
    """
    # Apply logarithm (base 10) to the 'IntCol' column
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the transformed 'IntCol' column to a list
    int_col_list = df['IntCol'].tolist()
    
    # Write the list to a 'IntCol.json' file
    with open('IntCol.json', 'w') as json_file:
        json.dump(int_col_list, json_file)
    
    return df