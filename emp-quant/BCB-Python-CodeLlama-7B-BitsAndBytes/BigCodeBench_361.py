
import pandas as pd
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.

    Args:
        sheet_name (str): The name of the sheet in the Excel file to read data from.
        excel_file_location (str, optional): The path to the Excel file. Defaults to "test.xlsx".
        csv_file_location (str, optional): The path to the CSV file. Defaults to "test.csv".

    Returns:
        dict: A dictionary with the sum of each column.

    Raises:
        FileNotFoundError: If the Excel file does not exist at the specified path.
        ValueError: If the specified sheet name is not found in the Excel file.
    """
    try:
        # Read the Excel file and convert it to a CSV file
        df = pd.read_excel(excel_file_location)
        df.to_csv(csv_file_location, index=False)

        # Calculate the sum of each column in the CSV file
        sums = {}
        for col in df.columns:
            sums[col] = df[col].sum()

        return sums

    except FileNotFoundError as e:
        logging.error(f"Excel file not found: {e}")
        raise e

    except ValueError as e:
        logging.error(f"Sheet name not found in Excel file: {e}")
        raise e