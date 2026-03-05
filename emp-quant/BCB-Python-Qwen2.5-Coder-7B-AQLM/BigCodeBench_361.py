
import pandas as pd
import logging
# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    try:
        # Read data from Excel file
        df = pd.read_excel(excel_file_location, sheet_name=sheet_name)
        
        # Convert the DataFrame to a CSV file
        df.to_csv(csv_file_location, index=False)
        logging.info(f"Data successfully converted to {csv_file_location}")
        
        # Calculate the sum of each column
        column_sums = df.sum().to_dict()
        logging.info("Column sums calculated successfully")
        
        return column_sums
    
    except FileNotFoundError:
        logging.error(f"File not found: {excel_file_location}")
        raise FileNotFoundError(f"The file {excel_file_location} does not exist.")
    
    except KeyError:
        logging.error(f"Sheet not found: {sheet_name}")
        raise ValueError(f"The sheet {sheet_name} does not exist in the file {excel_file_location}.")
    
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        raise e