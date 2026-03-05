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
    stats = {
        'sum': df[column].sum(),
        'mean': df[column].mean(),
        'min': df[column].min(),
        'max': df[column].max()
    }
    
    # Create pie chart
    fig, ax = plt.subplots()
    ax.pie(df[column].value_counts(), labels=df[column].unique(), autopct='%1.1f%%')
    ax.set_title(f'Pie Chart of {column}')
    
    return stats, ax