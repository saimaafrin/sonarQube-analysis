
import pandas as pd
import random

def task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42):
    # Create a Pandas DataFrame from the list of tuples
    df = pd.DataFrame(data, columns=columns)

    # Fill missing elements with None or random data
    if fill_missing:
        for i, row in df.iterrows():
            for j, cell in row.iteritems():
                if pd.isnull(cell):
                    if j == 'Quantity':
                        df.at[i, j] = random.randint(num_range[0], num_range[1])
                    else:
                        df.at[i, j] = None

    return df