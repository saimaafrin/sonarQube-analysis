
import pandas as pd
import logging
# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from Excel
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        logging.info(f"Data read successfully from {excel_file_location} sheet {sheet_name}")
        
        # Convert to CSV
        df.to_csv(csv_file_location, index=False)
        logging.info(f"Data converted to CSV and saved at {csv_file_location}")
        
        # Calculate the sum of each column
        column_sums = df.sum().to_dict()
        logging.info("Sum of each column calculated successfully")
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"File not found: {excel_file_location}")
        raise FileNotFoundError(f"File not found: {excel_file_location}")
    
    except KeyError:
        logging.error(f"Sheet not found: {sheet_name} in {excel_file_location}")
        raise ValueError(f"Sheet not found: {sheet_name} in {excel_file_location}")