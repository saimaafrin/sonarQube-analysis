import base64
import pandas as pd
def task_func(df):
    """
    Encodes a dict of list as a Base64 string.
    The dict is first converted to a Pandas DataFrame.
    Then convert the data frame to CSV format and encoded to bytes,
    finally encoded it to a Base64 string.
    """
    # Convert the dict to a Pandas DataFrame
    df = pd.DataFrame(df)

    # Convert the DataFrame to CSV format
    csv_data = df.to_csv(index=False)

    # Encode the CSV data to bytes
    csv_bytes = csv_data.encode()

    # Encode the bytes to a Base64 string
    base64_data = base64.b64encode(csv_bytes)

    # Return the Base64 encoded string
    return base64_data.decode()
df = {
    "col1": [1, 2, 3],
    "col2": ["a", "b", "c"],
    "col3": [4.5, 5.6, 6.7]
}