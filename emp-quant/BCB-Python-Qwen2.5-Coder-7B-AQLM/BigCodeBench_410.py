
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Construct the full file path
    file_path = os.path.join(excel_directory, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_name} does not exist in the directory {excel_directory}.")
    
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column {column_name} does not exist in the DataFrame.")
    
    # Convert start_date and end_date to datetime objects
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("The start_date or end_date is in an incorrect format. Please use the format 'YYYY-MM-DD'.")
    
    # Filter the DataFrame based on the date range
    filtered_df = df[(df[column_name] >= start_date) & (df[column_name] <= end_date)]
    
    return filtered_df