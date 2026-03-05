
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError

def task_func(csv_file_path, column_name, date_format="%Y-%m-%d"):
    # Check if the file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError("File not found")

    # Load the CSV file
    df = pd.read_csv(csv_file_path)

    # Check if the specified column is present
    if column_name not in df.columns:
        raise ValueError("Column not found")

    # Convert date values to datetime objects
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)

    # Filter rows based on the current date
    current_date = datetime.today().date()
    df = df[df[column_name].dt.date() == current_date]

    # Sort the resulting data
    df.sort_values(by=column_name, ascending=True, inplace=True)

    # Return the resulting DataFrame
    return df