
import pandas as pd
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from Excel spreadsheet
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert DataFrame to CSV file
        df.to_csv(csv_file_location, index=False)
        
        # Calculate the sum of each column
        column_sums = df.sum().to_dict()
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"FileNotFoundError: The file {excel_file_location} does not exist.")
        raise FileNotFoundError(f"The file {excel_file_location} does not exist.")
    
    except KeyError:
        logging.error(f"ValueError: Sheet '{sheet_name}' not found in the Excel file.")
        raise ValueError(f"Sheet '{sheet_name}' not found in the Excel file.")