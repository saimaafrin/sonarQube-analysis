
import json
import numpy as np
import pandas as pd

def task_func(df):
    # Apply the logarithm (base 10) transformation to the 'IntCol' column
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Write the transformed 'IntCol' column to a JSON file as a list
    df['IntCol'].to_json('IntCol.json', orient='records', lines=True)
    
    # Return the DataFrame with the transformed 'IntCol' column
    return df