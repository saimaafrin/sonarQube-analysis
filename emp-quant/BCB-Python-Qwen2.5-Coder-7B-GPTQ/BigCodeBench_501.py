import xlwt
import os
import pandas as pd
def task_func(json_str, filename, sheet_name="sheet1"):
    # Check if json_str is a string
    if not isinstance(json_str, (str, bytes, bytearray)):
        raise TypeError("json_str must be a string, bytes, or bytearray")
    
    # Try to parse the JSON string
    try:
        data = pd.read_json(json_str)
    except ValueError:
        raise ValueError("Invalid JSON string")
    
    # Create a Pandas DataFrame from the JSON data
    df = pd.DataFrame(data)
    
    # Create a new Excel writer using xlwt
    writer = pd.ExcelWriter(filename, engine='xlwt')
    
    # Write the DataFrame to the Excel file
    df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Save the Excel file
    writer.save()
    
    # Return the absolute path of the created Excel file
    return os.path.abspath(filename)