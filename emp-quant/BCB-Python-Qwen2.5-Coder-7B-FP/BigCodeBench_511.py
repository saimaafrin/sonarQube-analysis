import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Check if the column exists in the DataFrame
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in the data.")
    
    # Calculate statistics
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Create a dictionary with the statistics
    stats = {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value
    }
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(df[column], labels=df[column], autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return stats, ax