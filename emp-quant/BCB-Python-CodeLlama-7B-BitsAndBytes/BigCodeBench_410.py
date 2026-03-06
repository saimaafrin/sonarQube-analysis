
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.

    Parameters
    ----------
    excel_directory : str
        The directory where the Excel file is located.
    file_name : str
        The name of the Excel file.
    column_name : str
        The name of the column to filter.
    start_date : str
        The start date of the date range.
    end_date : str
        The end date of the date range.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame with the filtered data.

    Raises
    ------
    FileNotFoundError
        If the specified Excel file does not exist.
    ValueError
        If start_date or end_date are in an incorrect format, or if column_name does not exist in the DataFrame.
    """
    # Check if the Excel file exists
    if not os.path.exists(os.path.join(excel_directory, file_name)):
        raise FileNotFoundError(f"Excel file {file_name} does not exist in directory {excel_directory}")

    # Check if start_date and end_date are in the correct format
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Start date {start_date} or end date {end_date} are in an incorrect format")

    # Check if column_name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the DataFrame")

    # Filter the data
    df = df[df[column_name].between(start_date, end_date)]

    return df