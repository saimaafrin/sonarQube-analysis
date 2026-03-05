
import os
import pandas as pd
from datetime import datetime
from typing import List

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Check if the Excel file exists
    if not os.path.exists(os.path.join(excel_directory, file_name)):
        raise FileNotFoundError(f"File {file_name} not found in directory {excel_directory}")

    # Load the Excel file into a DataFrame
    df = pd.read_excel(os.path.join(excel_directory, file_name))

    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} not found in the DataFrame")

    # Convert start_date and end_date to datetime objects
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format. Please use YYYY-MM-DD.")

    # Filter the DataFrame based on the date range
    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]

    return filtered_df