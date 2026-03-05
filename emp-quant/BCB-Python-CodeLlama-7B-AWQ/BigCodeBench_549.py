import base64
import pandas as pd
def task_func(df):
    """
    Encodes a dict of list as a Base64 string.
    The dict is first converted to a Pandas DataFrame.
    Then convert the data frame to CSV format and encoded to bytes,
    finally encoded it to a Base64 string.
    The function should output with:
        str: The Base64 encoded string of the DataFrame's CSV representation.
    """
    # Convert the dict to a Pandas DataFrame
    df = pd.DataFrame(df)

    # Convert the DataFrame to CSV format and encode it to bytes
    csv_bytes = df.to_csv(index=False).encode()

    # Encode the CSV bytes to a Base64 string
    base64_str = base64.b64encode(csv_bytes).decode()

    return base64_str
df = {'a': [1, 2, 3], 'b': [4, 5, 6]}