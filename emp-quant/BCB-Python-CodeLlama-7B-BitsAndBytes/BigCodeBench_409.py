
import os
import pandas as pd
import numpy as np

def task_func(excel_file_path, file_name, column_name):
    """
    Calculate the mean, median, and standard deviation of the data from a specific column in an Excel file.

    Args:
        excel_file_path (str): The path to the Excel file.
        file_name (str): The name of the Excel file.
        column_name (str): The name of the column to calculate the statistics for.

    Returns:
        dict: A dictionary with the mean, median, and standard deviation.

    Raises:
        FileNotFoundError: If the Excel file does not exist at the specified path.
        ValueError: If the specified column is not found in the Excel file.
    """
    # Check if the Excel file exists
    if not os.path.exists(excel_file_path):
        raise FileNotFoundError(f"Excel file {file_name} not found at {excel_file_path}")

    # Read the Excel file using pandas
    df = pd.read_excel(excel_file_path)

    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in Excel file {file_name}")

    # Calculate the mean, median, and standard deviation of the specified column
    mean = df[column_name].mean()
    median = df[column_name].median()
    std = df[column_name].std()

    # Create a dictionary with the results
    results = {"mean": mean, "median": median, "std": std}

    return results