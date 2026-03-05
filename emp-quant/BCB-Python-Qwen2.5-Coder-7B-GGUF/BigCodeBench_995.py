
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    # Read the CSV file
    data = pd.read_csv(file_path)
    
    # Clean the data by removing non-numeric values
    numeric_data = data.apply(pd.to_numeric, errors='coerce')
    
    # Calculate mean and median
    mean_value = numeric_data.mean().iloc[0]
    median_value = numeric_data.median().iloc[0]
    
    # Plot the data
    plt.figure()
    plt.plot(numeric_data)
    plt.title("Data Visualization")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.savefig(plot_path)
    
    # Return the results
    return (mean_value, median_value, plot_path)