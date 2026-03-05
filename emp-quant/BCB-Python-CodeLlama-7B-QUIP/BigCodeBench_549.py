
import base64
import pandas as pd

def task_func(df):
    # Convert the DataFrame to a CSV string
    csv_str = df.to_csv(index=False, header=False, sep=",")

    # Encode the CSV string to bytes
    bytes_str = csv_str.encode("utf-8")

    # Encode the bytes to a Base64 string
    base64_str = base64.b64encode(bytes_str)

    return base64_str.decode("utf-8")