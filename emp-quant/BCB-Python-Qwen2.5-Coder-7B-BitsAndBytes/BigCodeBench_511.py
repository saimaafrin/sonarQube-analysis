
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def task_func(column, data):
    # Check if the data list is empty
    if not data:
        return ({}, None)
    
    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    
    # Calculate the required statistics
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(df[column], labels=df['Age'], autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    return (stats, ax)