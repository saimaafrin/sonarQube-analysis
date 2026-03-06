
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if not data:
        raise ValueError("Data list is empty")
    
    # Convert the list to a DataFrame
    df = pd.DataFrame(data)
    
    # Check if the specified column exists
    if column not in df.columns:
        raise KeyError(f"Invalid column name: {column}")
    
    # Validate numeric values for steps, calories burned, and distance walked
    if column in ['steps', 'calories_burned', 'distance_walked']:
        if (df[column] < 0).any():
            raise ValueError(f"{column} cannot be negative")
    
    # Calculate sum, mean, min, and max of the column
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Draw a line chart
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df[column], marker='o')
    ax.set_title(f'Line Chart of {column}')
    ax.set_xlabel('Date')
    ax.set_ylabel(column)
    
    return stats, ax