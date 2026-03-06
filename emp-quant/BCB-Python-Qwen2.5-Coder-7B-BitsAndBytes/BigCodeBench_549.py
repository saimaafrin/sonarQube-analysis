
import base64
import pandas as pd

def task_func(data_dict):
    # Convert the dictionary to a Pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Convert the DataFrame to CSV format
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    # Encode the CSV data to Base64
    base64_encoded = base64.b64encode(csv_data).decode('utf-8')
    
    return base64_encoded