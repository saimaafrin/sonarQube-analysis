import json
import numpy as np
import pandas as pd
def task_func(df):
    """
    Transforms the 'IntCol' column of the given DataFrame by applying a logarithm (base 10) to each value,
    and then writes the transformed column as a list to a 'IntCol.json' file.
    
    Parameters:
    df (DataFrame): A pandas DataFrame with a column named 'IntCol'.
    
    Returns:
    DataFrame: The original DataFrame with the 'IntCol' transformed.
    """
    # Apply logarithm (base 10) to the 'IntCol' column
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the transformed column to a list
    transformed_list = df['IntCol'].tolist()
    
    # Write the list to a 'IntCol.json' file
    with open('IntCol.json', 'w') as json_file:
        json.dump(transformed_list, json_file)
    
    return df