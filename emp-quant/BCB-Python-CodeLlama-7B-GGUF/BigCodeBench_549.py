
import base64
import pandas as pd

def task_func(df):
    # Convert the dict to a Pandas DataFrame
    df = pd.DataFrame(df)

    # Convert the DataFrame to CSV format
    csv = df.to_csv(index=False)

    # Encode the CSV data to bytes
    csv_bytes = csv.encode('utf-8')

    # Encode the bytes to a Base64 string
    base64_str = base64.b64encode(csv_bytes)

    # Return the Base64 encoded string
    return base64_str.decode('utf-8')