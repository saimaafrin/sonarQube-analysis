
import os
import pandas as pd
import numpy as np

def task_func(excel_file_path, file_name, column_name):
    # Check if the Excel file exists
    if not os.path.exists(os.path.join(excel_file_path, file_name)):
        raise FileNotFoundError(f"Excel file '{file_name}' not found at path '{excel_file_path}'")
    
    # Load the Excel file
    file_path = os.path.join(excel_file_path, file_name)
    df = pd.read_excel(file_path)
    
    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the Excel file")
    
    # Calculate mean, median, and standard deviation
    mean = df[column_name].mean()
    median = df[column_name].median()
    std_dev = df[column_name].std()
    
    # Return the results as a dictionary
    return {
        'mean': mean,
        'median': median,
        'standard_deviation': std_dev
    }