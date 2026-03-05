
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError("The specified file does not exist.")
    
    # Load the Excel file
    try:
        df = pd.read_excel(file_location, sheet_name=sheet_name)
    except KeyError:
        raise ValueError("The specified sheet does not exist in the workbook.")
    
    # Calculate mean and standard deviation for each column
    stats = df.describe().loc[['mean', 'std']]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(df.columns, stats.loc['mean'], yerr=stats.loc['std'], capsize=5)
    ax.set_title('Mean and Standard Deviation')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')
    
    return stats, fig