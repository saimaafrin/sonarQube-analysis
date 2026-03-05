
import pandas as pd
import random

def task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42):
    # Create a Pandas DataFrame from a list of tuples
    df = pd.DataFrame(data, columns=columns)

    # Fill missing elements with None or random data
    if fill_missing:
        for col in df.columns:
            df[col] = df[col].fillna(random.randint(0, 100))

    return df