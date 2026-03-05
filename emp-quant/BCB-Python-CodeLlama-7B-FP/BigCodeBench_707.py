import json
import numpy as np
import pandas as pd
def task_func(df):
    """
    Given a DataFrame with random values and an 'IntCol' column, transform the 'IntCol' column by a logarithm (base 10) and write it to a `IntCol.json` file as a list. Also return the DataFrame.
    """
    # Transform the 'IntCol' column by a logarithm (base 10)
    df['IntCol'] = np.log10(df['IntCol'])

    # Write the transformed 'IntCol' column to a JSON file
    with open('IntCol.json', 'w') as f:
        json.dump(df['IntCol'].tolist(), f)

    return df
df = pd.DataFrame({'IntCol': np.random.randint(1, 100, size=10)})