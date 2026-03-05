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
    df = pd.read_excel(excel_file_path, usecols=[column_name])
    mean = df.mean()
    median = df.median()
    std = df.std()

    # Return a dictionary with the mean, median, and standard deviation
    return {"mean": mean, "median": median, "std": std}
excel_file_path = "example.xlsx"
file_name = "example"
column_name = "column1"