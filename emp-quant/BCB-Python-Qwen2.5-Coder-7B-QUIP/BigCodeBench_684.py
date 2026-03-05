
import pandas as pd
import numpy as np

def task_func(df, col):
    # Remove the specified column from the DataFrame
    df = df.drop(columns=[col])
    
    # Add a new column 'IsEvenIndex' indicating if the index is even
    df['IsEvenIndex'] = df.index % 2 == 0
    
    return df