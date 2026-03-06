
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def task_func(file_path: str, plot_path: str) -> (float, float, str):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Read the CSV file
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")
    
    # Clean the data: remove non-numeric values
    numeric_data = df.select_dtypes(include=[np.number])
    
    # Calculate mean and median
    mean_value = numeric_data.mean().values[0] if not numeric_data.empty else np.nan
    median_value = numeric_data.median().values[0] if not numeric_data.empty else np.nan
    
    # Generate a plot
    plt.figure()
    plt.plot(numeric_data.values.flatten(), label='Values')
    plt.title('Data Visualization')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig(plot_path)
    
    return mean_value, median_value, plot_path