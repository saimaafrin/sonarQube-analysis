
import pandas as pd
import numpy as np

def task_func(df, col):
    # Remove the specified column
    df = df.drop(columns=[col])

    # Add a new column 'IsEvenIndex'
    df['IsEvenIndex'] = np.where(df.index % 2 == 0, True, False)

    return df