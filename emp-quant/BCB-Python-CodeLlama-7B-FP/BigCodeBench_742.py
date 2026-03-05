import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_pairs):
    """
    Create a Pandas DataFrame from a list of pairs and normalize the data using MinMaxScaler.
    The function should raise the exception for:
        - Exception: If the input array is empty.
        - ValueError: If Values are not numeric.
    The function should output with:
        - DataFrame:  A pandas DataFrame containing the columns 'Category' and 'Value'.
        - Category contains the the first elements of each tuple.
        - Value contains the normalized values of each tuple.
    """
    # Check if the input list is empty
    if not list_of_pairs:
        raise Exception("Input list is empty")

    # Check if the values are numeric
    for pair in list_of_pairs:
        if not isinstance(pair[1], (int, float)):
            raise ValueError("Values are not numeric")

    # Create a DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=["Category", "Value"])

    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    df["Value"] = scaler.fit_transform(df["Value"].values.reshape(-1, 1))

    return df
list_of_pairs = [("A", 1), ("B", 2), ("C", 3)]