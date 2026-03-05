import pandas as pd
import logging
def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        # Convert to CSV
        df.to_csv(csv_file_location, index=False)
        # Calculate sum of each column
        sums = df.sum(axis=0)
        # Return dictionary with sum of each column
        return {col: sum for col, sum in sums.items()}
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logging.error(f"Sheet name not found: {e}")
        raise