
import json
import numpy as np
import pandas as pd

def task_func(df):
    # Transform the 'IntCol' column by a logarithm (base 10)
    df['IntCol'] = np.log10(df['IntCol'])

    # Write the transformed data to a JSON file
    with open('IntCol.json', 'w') as f:
        json.dump(df['IntCol'].tolist(), f)

    return df