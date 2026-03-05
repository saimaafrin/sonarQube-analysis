
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError

def task_func(csv_file_path, column_name, date_format="%Y-%m-%d"):
    """
    Reads a CSV file and processes its date-related data.

    Parameters
    ----------
    csv_file_path : str
        Path to the CSV file.
    column_name : str
        Name of the column containing the date values.
    date_format : str, optional
        Format of the date values in the CSV file. Default is "%Y-%m-%d".

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the processed date data.

    Raises
    ------
    FileNotFoundError
        If the specified CSV file is not found at the given path.
    ValueError
        If the specified column is not present in the CSV file.
    """
    # Check if the CSV file exists
    if not os.path.isfile(csv_file_path):
        raise FileNotFoundError(f"File not found: {csv_file_path}")

    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Check if the specified column is present in the CSV file
    if column_name not in df.columns:
        raise ValueError(f"Column not found: {column_name}")

    # Convert date values to datetime objects
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)

    # Filter rows based on the current date
    today = datetime.today().date()
    df = df[df[column_name] == today]

    # Sort the resulting data
    df.sort_values(by=column_name, ascending=True, inplace=True)

    # Return the processed data
    return df