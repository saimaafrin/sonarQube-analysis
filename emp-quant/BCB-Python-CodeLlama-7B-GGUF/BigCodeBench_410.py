
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.

    Parameters:
    excel_directory (str): The directory where the Excel file is located.
    file_name (str): The name of the Excel file.
    column_name (str): The name of the column to filter data from.
    start_date (str): The start date of the date range to filter data from, in the format 'YYYY-MM-DD'.
    end_date (str): The end date of the date range to filter data from, in the format 'YYYY-MM-DD'.

    Returns:
    pd.DataFrame: A pandas DataFrame with the filtered data.

    Raises:
    FileNotFoundError: If the specified Excel file does not exist.
    ValueError: If start_date or end_date are in an incorrect format, or if column_name does not exist in the DataFrame.
    """
    # Check if the Excel file exists
    if not os.path.isfile(os.path.join(excel_directory, file_name)):
        raise FileNotFoundError(f"The Excel file {file_name} does not exist in the directory {excel_directory}.")

    # Check if start_date and end_date are in the correct format
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"The start_date and end_date must be in the format 'YYYY-MM-DD'.")

    # Check if column_name exists in the DataFrame
    if column_name not in pd.read_excel(os.path.join(excel_directory, file_name), nrows=1).columns:
        raise ValueError(f"The column {column_name} does not exist in the Excel file {file_name}.")

    # Filter data based on the date range and column name
    df = pd.read_excel(os.path.join(excel_directory, file_name))
    df = df[df[column_name].between(start_date, end_date)]

    return df