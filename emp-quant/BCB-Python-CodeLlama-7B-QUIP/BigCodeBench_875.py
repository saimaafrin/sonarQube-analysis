
import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    # Create a Pandas DataFrame from a list of tuples
    df = pd.DataFrame(data, columns=columns)

    # Fill missing elements with None or random data
    if fill_missing:
        for col in columns:
            if col in df.columns:
                df[col] = df[col].fillna(random.randint(num_range[0], num_range[1]))

    return df