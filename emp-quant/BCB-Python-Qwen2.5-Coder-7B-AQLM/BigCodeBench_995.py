
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        
        # Clean the data by removing non-numeric values
        numeric_data = data.apply(pd.to_numeric, errors='coerce')
        
        # Calculate mean and median
        mean_value = np.nanmean(numeric_data)
        median_value = np.nanmedian(numeric_data)
        
        # Plot the data
        plt.figure(figsize=(10, 5))
        plt.plot(numeric_data, marker='o')
        plt.title("Data Visualization")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.savefig(plot_path)
        
        return mean_value, median_value, plot_path
    
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} does not exist.")