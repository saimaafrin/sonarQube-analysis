
import pandas as pd
import numpy as np

def task_func(df, col):
    # Remove the specified column
    df = df.drop(col, axis=1)

    # Add a new column with the IsEvenIndex flag
    df['IsEvenIndex'] = np.mod(df.index, 2) == 0

    return df