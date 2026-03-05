
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Check if the Excel file exists
    if not os.path.exists(excel_directory + file_name):
        raise FileNotFoundError("The specified Excel file does not exist")

    # Check if the start_date and end_date are in the correct format
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("The start_date and end_date must be in the format YYYY-MM-DD")

    # Read the Excel file
    df = pd.read_excel(excel_directory + file_name)

    # Filter the data in the specified column
    df = df[column_name].loc[start_date:end_date]

    return df