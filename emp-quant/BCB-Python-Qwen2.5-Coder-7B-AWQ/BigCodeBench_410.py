import os
import pandas as pd
from datetime import datetime
def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Construct the full file path
    file_path = os.path.join(excel_directory, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified Excel file does not exist: {file_path}")
    
    # Read the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Check if the column_name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The specified column_name does not exist in the DataFrame: {column_name}")
    
    # Convert the start_date and end_date to datetime objects
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The start_date or end_date are in an incorrect format. Please use 'YYYY-MM-DD' format.")
    
    # Filter the data in the specified date range
    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]
    
    return filtered_df