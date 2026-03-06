
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def task_func(file_location, sheet_name):
    # Check if the file exists
    if not os.path.exists(file_location):
        raise FileNotFoundError("Excel file does not exist at the specified path.")
    
    try:
        # Load the Excel file
        df = pd.read_excel(file_location, sheet_name=sheet_name)
        
        # Calculate mean and standard deviation
        stats = {
            'mean': df.mean(),
            'std_dev': df.std()
        }
        
        # Create a bar chart
        fig, ax = plt.subplots()
        ax.bar(stats['mean'].index, stats['mean'], yerr=stats['std_dev'])
        ax.set_title('Mean and Standard Deviation')
        ax.set_xlabel('Columns')
        ax.set_ylabel('Values')
        
        return stats, fig
    
    except KeyError:
        raise ValueError("Specified sheet does not exist in the workbook.")