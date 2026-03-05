
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=[column])
    
    # Calculate statistics
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Handle empty data case
    if df[column].empty:
        stats['sum'] = 0
        stats['mean'] = np.nan
        stats['min'] = np.nan
        stats['max'] = np.nan
    
    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(df[column].value_counts(), labels=df[column].unique(), autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return stats, ax