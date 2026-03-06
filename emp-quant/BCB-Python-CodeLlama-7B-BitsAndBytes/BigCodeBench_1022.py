
import pandas as pd
import os
from datetime import datetime
from pandas.errors import EmptyDataError

def task_func(csv_file_path, column_name, date_format="%Y-%m-%d"):
    # Check if the CSV file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File not found: {csv_file_path}")

    # Read the CSV file and convert the date column to datetime objects
    df = pd.read_csv(csv_file_path, parse_dates=[column_name])
    df[column_name] = pd.to_datetime(df[column_name], format=date_format)

    # Filter the rows based on the current date
    current_date = datetime.today().strftime(date_format)
    df = df[df[column_name] == current_date]

    # Sort the data by the date column
    df.sort_values(by=column_name, inplace=True)

    # Return the filtered and sorted DataFrame
    return df