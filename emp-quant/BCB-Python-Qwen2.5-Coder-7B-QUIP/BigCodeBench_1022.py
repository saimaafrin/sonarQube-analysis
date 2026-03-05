
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError

def task_func(csv_file_path, column_name, date_format="%Y-%m-%d"):
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File not found: {csv_file_path}")

    # Read the CSV file into a DataFrame
    try:
        df = pd.read_csv(csv_file_path)
    except EmptyDataError:
        return pd.DataFrame()

    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column not found: {column_name}")

    # Convert the date column to datetime objects
    df[column_name] = pd.to_datetime(df[column_name], format=date_format, errors='coerce')

    # Filter rows based on the current date
    today = datetime.today().date()
    df = df[df[column_name].dt.date == today]

    # Sort the resulting data
    df = df.sort_values(by=column_name)

    return df