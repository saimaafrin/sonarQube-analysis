
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    # Construct the full path to the Excel file
    file_path = os.path.join(excel_directory, file_name)
    
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_name} does not exist in the directory {excel_directory}.")
    
    # Load the Excel file into a DataFrame
    df = pd.read_excel(file_path)
    
    # Convert the start_date and end_date strings to datetime objects
    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("start_date and end_date must be in 'YYYY-MM-DD' format.")
    
    # Check if the column_name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Filter the DataFrame based on the date range
    filtered_df = df[(df[column_name] >= start_date_dt) & (df[column_name] <= end_date_dt)]
    
    return filtered_df