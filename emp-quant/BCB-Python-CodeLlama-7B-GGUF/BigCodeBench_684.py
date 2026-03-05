
import pandas as pd
import numpy as np

def task_func(df, col):
    # Remove the specified column
    df.drop(columns=col, inplace=True)
    
    # Add a new column 'IsEvenIndex'
    df['IsEvenIndex'] = df.index % 2 == 0
    
    return df