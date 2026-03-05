import os
import pandas as pd
from datetime import datetime
def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.
    """
    # Check if the Excel file exists
    if not os.path.exists(excel_directory):
        raise FileNotFoundError(f"The Excel file {excel_directory} does not exist.")

    # Check if the column name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column {column_name} does not exist in the DataFrame.")

    # Check if the start and end dates are in the correct format
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"The start and end dates must be in the format YYYY-MM-DD.")

    # Filter the data
    df_filtered = df[df[column_name].between(start_date, end_date)]

    return df_filtered
excel_directory = "path/to/excel/file.xlsx"
file_name = "file_name.xlsx"
column_name = "date_column"
start_date = "2022-01-01"
end_date = "2022-01-31"
df = pd.read_excel(excel_directory, file_name)