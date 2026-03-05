import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError("The specified file does not exist at the given path.")
    
    # Load the Excel file
    try:
        df = pd.read_excel(file_location, sheet_name=sheet_name)
    except KeyError:
        raise ValueError("The specified sheet does not exist in the workbook.")
    
    # Calculate mean and standard deviation
    stats = {
        'mean': df.mean().to_dict(),
        'std': df.std().to_dict()
    }
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(stats['mean'].keys(), stats['mean'].values(), label='Mean')
    ax.bar(stats['std'].keys(), stats['std'].values(), label='Standard Deviation', alpha=0.7)
    ax.set_title('Mean and Standard Deviation')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Values')
    ax.legend()
    
    return stats, fig