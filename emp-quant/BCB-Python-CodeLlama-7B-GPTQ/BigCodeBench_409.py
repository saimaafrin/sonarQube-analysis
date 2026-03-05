import os
import pandas as pd
import numpy as np
def task_func(excel_file_path, file_name, column_name):
    """
    Calculate the mean, median, and standard deviation of the data from a specific column in an Excel file.
    """
    # Check if the Excel file exists
    if not os.path.exists(excel_file_path):
        raise FileNotFoundError(f"Excel file {excel_file_path} does not exist")

    # Check if the specified column exists
    if column_name not in pd.read_excel(excel_file_path, nrows=1).columns:
        raise ValueError(f"Column {column_name} not found in Excel file {excel_file_path}")

    # Calculate the mean, median, and standard deviation
    df = pd.read_excel(excel_file_path)
    mean = df[column_name].mean()
    median = df[column_name].median()
    std = df[column_name].std()

    # Return the results as a dictionary
    return {
        "mean": mean,
        "median": median,
        "std": std,
    }
excel_file_path = "data.xlsx"
file_name = "Sheet1"
column_name = "Column1"