
import os
import pandas as pd
import numpy as np

def task_func(excel_file_path, file_name, column_name):
    try:
        # Construct the full file path
        file_path = os.path.join(excel_file_path, file_name)
        
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_name} does not exist at the specified path {excel_file_path}")
        
        # Read the Excel file
        df = pd.read_excel(file_path)
        
        # Check if the specified column exists
        if column_name not in df.columns:
            raise ValueError(f"The column {column_name} is not found in the Excel file")
        
        # Calculate mean, median, and standard deviation
        mean_value = df[column_name].mean()
        median_value = df[column_name].median()
        std_deviation = df[column_name].std()
        
        # Return the results in a dictionary
        return {
            'mean': mean_value,
            'median': median_value,
            'standard_deviation': std_deviation
        }
    
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e