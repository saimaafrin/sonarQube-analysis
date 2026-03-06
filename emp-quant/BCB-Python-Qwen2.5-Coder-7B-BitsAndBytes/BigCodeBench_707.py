
import json
import numpy as np
import pandas as pd

def task_func(df):
    # Apply log base 10 transformation to 'IntCol'
    df['IntCol'] = np.log10(df['IntCol'])
    
    # Convert the DataFrame to a list of dictionaries
    result_list = df.to_dict(orient='records')
    
    # Write the list to a JSON file
    with open('IntCol.json', 'w') as f:
        json.dump(result_list, f)
    
    return df