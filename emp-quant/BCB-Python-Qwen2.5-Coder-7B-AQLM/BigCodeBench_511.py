
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    if not data:
        return {'sum': 0, 'mean': np.nan, 'min': np.nan, 'max': np.nan}, plt.figure().add_subplot(111)
    
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Calculate statistics
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(df[column], labels=df[column], autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return stats, ax