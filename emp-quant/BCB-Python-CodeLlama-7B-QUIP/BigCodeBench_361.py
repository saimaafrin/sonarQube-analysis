
import pandas as pd
import logging
# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file_location)
        # Convert to CSV
        df.to_csv(csv_file_location, index=False)
        # Calculate the sum of each column
        sums = {}
        for column in df.columns:
            sums[column] = df[column].sum()
        return sums
    except FileNotFoundError:
        logging.error("Excel file not found")
        raise FileNotFoundError
    except ValueError:
        logging.error("Sheet name not found")
        raise ValueError