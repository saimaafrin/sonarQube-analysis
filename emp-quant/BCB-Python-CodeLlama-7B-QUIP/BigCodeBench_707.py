
import json
import numpy as np

def task_func(df):
    # Perform logarithm on the IntCol column
    df['IntCol'] = np.log10(df['IntCol'])
    # Write the transformed data to a JSON file
    with open('IntCol.json', 'w') as outfile:
        json.dump(df['IntCol'].tolist(), outfile)
    return df