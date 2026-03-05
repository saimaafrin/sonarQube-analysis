import os
import pandas as pd
import numpy as np
def task_func(excel_file_path, file_name, column_name):
    # Construct the full file path
    file_path = os.path.join(excel_file_path, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_name} does not exist at the specified path {excel_file_path}.")
    
    # Load the Excel file
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"Error reading the Excel file: {e}")
    
    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"The column {column_name} is not found in the Excel file.")
    
    # Calculate mean, median, and standard deviation
    mean_value = df[column_name].mean()
    median_value = df[column_name].median()
    std_deviation = df[column_name].std()
    
    # Return the results as a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'std_deviation': std_deviation
    }