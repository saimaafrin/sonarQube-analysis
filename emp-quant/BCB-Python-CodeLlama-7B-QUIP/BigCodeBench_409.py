
import os
import pandas as pd
import numpy as np

def task_func(excel_file_path, file_name, column_name):
    # Check if the Excel file exists
    if not os.path.exists(excel_file_path):
        raise FileNotFoundError("Excel file not found")

    # Read the Excel file
    df = pd.read_excel(excel_file_path)

    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError("Column not found")

    # Calculate the mean, median, and standard deviation
    mean = df[column_name].mean()
    median = df[column_name].median()
    std = df[column_name].std()

    # Return a dictionary with the mean, median, and standard deviation
    return {
        "mean": mean,
        "median": median,
        "std": std
    }