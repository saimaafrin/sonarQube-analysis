import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(column, data):
    # Create a DataFrame from the data
    df = pd.DataFrame(data, columns=[column])
    
    # Calculate the sum, mean, min, and max of the column
    sum_value = df[column].sum()
    mean_value = df[column].mean()
    min_value = df[column].min()
    max_value = df[column].max()
    
    # Create a dictionary with the calculated statistics
    stats = {
        'sum': sum_value,
        'mean': mean_value,
        'min': min_value,
        'max': max_value
    }
    
    # Create a pie chart using the Age column as labels
    fig, ax = plt.subplots()
    ax.pie(df[column], labels=df[column], autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    # Return the tuple containing the dictionary and the Axes object
    return (stats, ax)