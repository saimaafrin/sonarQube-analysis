
import json
import numpy as np
import pandas as pd

def task_func(df):
    # Apply logarithm base 10 to the 'IntCol' column
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the DataFrame to a list of dictionaries
    df_list = df.to_dict(orient='records')
    
    # Write the list to a JSON file
    with open('IntCol.json', 'w') as f:
        json.dump(df_list, f)
    
    return df