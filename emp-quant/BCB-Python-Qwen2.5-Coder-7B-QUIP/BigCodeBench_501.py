
import xlwt
import os
import pandas as pd

def task_func(json_str, filename, sheet_name="sheet1"):
    # Validate the input
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray")
    
    try:
        # Load the JSON string into a pandas DataFrame
        data = pd.read_json(json_str, error='raise')
        
        # Create a new Excel writer
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        
        # Write the DataFrame to the Excel file
        data.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Close the writer
        writer.close()
        
        # Return the absolute path of the created Excel file
        return os.path.abspath(filename)
    
    except ValueError as e:
        raise ValueError("Invalid JSON string") from e
    except Exception as e:
        raise Exception("Error writing to Excel file") from e