import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Convert the data list to a DataFrame
    df = pd.DataFrame(data, columns=['date', 'temperature', 'humidity', 'wind speed', 'precipitation'])
    
    # Check if the DataFrame is empty
    if df.empty:
        result = {
            'sum': np.nan,
            'mean': np.nan,
            'min': np.inf,
            'max': -np.inf,
            'plot': None
        }
    else:
        # Calculate the required statistics
        result = {
            'sum': df[column].sum(),
            'mean': df[column].mean(),
            'min': df[column].min(),
            'max': df[column].max(),
            'plot': df[column].hist()
        }
    
    return result