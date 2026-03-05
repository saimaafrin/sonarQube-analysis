import pandas as pd
import logging
def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_file_location)
        # Convert to CSV
        df.to_csv(csv_file_location, index=False)
        # Calculate sum of each column
        sums = {}
        for col in df.columns:
            sums[col] = df[col].sum()
        return sums
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
        raise
    except ValueError as e:
        logging.error(f"Sheet not found: {e}")
        raise