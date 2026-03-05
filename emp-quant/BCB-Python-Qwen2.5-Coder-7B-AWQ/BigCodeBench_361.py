import pandas as pd
import logging
def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.
    
    Args:
    sheet_name (str): The name of the sheet to read from the Excel file.
    excel_file_location (str): The path to the Excel file.
    csv_file_location (str): The path where the CSV file will be saved.
    
    Returns:
    dict: A dictionary with the sum of each column.
    
    Raises:
    FileNotFoundError: If the Excel file does not exist at the specified path.
    ValueError: If the specified sheet name is not found in the Excel file.
    """
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
    except FileNotFoundError:
        logging.error(f"File not found: {excel_file_location}")
        raise FileNotFoundError(f"File not found: {excel_file_location}")
    except KeyError:
        logging.error(f"Sheet not found: {sheet_name}")
        raise ValueError(f"Sheet not found: {sheet_name}")
    
    # Convert the DataFrame to a CSV file
    df.to_csv(csv_file_location, index=False)
    
    # Calculate the sum of each column
    column_sums = df.sum().to_dict()
    
    return column_sums