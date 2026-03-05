import pandas as pd
import logging
def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from Excel file
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert DataFrame to CSV file
        df.to_csv(csv_file_location, index=False)
        
        # Calculate the sum of each column
        column_sums = df.sum().to_dict()
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"File not found: {excel_file_location}")
        raise FileNotFoundError(f"Excel file not found at the specified path: {excel_file_location}")
    
    except KeyError:
        logging.error(f"Sheet not found: {sheet_name}")
        raise ValueError(f"Specified sheet name '{sheet_name}' not found in the Excel file.")