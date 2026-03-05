import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Check if the data list is empty
    if not data:
        raise ValueError("Data list is empty")
    
    # Convert the data list to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column is valid
    if column not in df.columns:
        raise KeyError("Invalid column name")
    
    # Check if the numeric values for steps, calories burned, and distance walked are non-negative
    if column in ['steps', 'calories_burned', 'distance_walked']:
        if (df[column] < 0).any():
            raise ValueError("Numeric values for steps, calories burned, and distance walked must be non-negative")
    
    # Calculate the sum, mean, min, and max of the column
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Draw a line chart
    fig, ax = plt.subplots()
    ax.plot(df['date'], df[column], marker='o')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    ax.set_title(f'Line Chart of {column}')
    
    return (stats, ax)