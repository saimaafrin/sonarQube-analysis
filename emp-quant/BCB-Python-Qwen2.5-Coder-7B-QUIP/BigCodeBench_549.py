
import base64
import pandas as pd

def task_func(df):
    # Convert the DataFrame to CSV format
    csv_str = df.to_csv(index=False)
    
    # Encode the CSV string to bytes
    csv_bytes = csv_str.encode('utf-8')
    
    # Encode the bytes to a Base64 string
    base64_bytes = base64.b64encode(csv_bytes)
    
    # Convert the Base64 bytes to a string
    base64_str = base64_bytes.decode('utf-8')
    
    return base64_str