
import pandas as pd
import logging
# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from Excel
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert to CSV
        df.to_csv(csv_file_location, index=False)
        
        # Calculate the sum of each column
        column_sums = df.sum()
        
        # Return the sum of each column as a dictionary
        return column_sums.to_dict()
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found at {excel_file_location}")
    
    except KeyError:
        raise ValueError(f"Sheet name {sheet_name} not found in the Excel file")