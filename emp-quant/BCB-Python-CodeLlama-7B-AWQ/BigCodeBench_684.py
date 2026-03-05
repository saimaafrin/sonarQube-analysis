import pandas as pd
import numpy as np
def task_func(df, col):
    """
    Process a Pandas DataFrame by removing a specific column and adding a 'IsEvenIndex' column.
    The 'IsEvenIndex' column is a boolean flag indicating if the index of each row is even.
    """
    # Remove the specified column
    df = df.drop(columns=[col])

    # Add a new 'IsEvenIndex' column
    df['IsEvenIndex'] = df.index % 2 == 0

    return df
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})