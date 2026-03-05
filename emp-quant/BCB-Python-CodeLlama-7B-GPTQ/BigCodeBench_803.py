import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(file_name: str) -> pd.DataFrame:
    """
    Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as they are.
    The function should raise the exception for: ValueError: If input does not have numeric columns.
    The function should output with:
        DataFrame: A pandas DataFrame with normalized data.
    """
    # Load the data from the csv file
    data = pd.read_csv(file_name)

    # Check if the data has any numeric columns
    if not data.select_dtypes(include=[np.number]).shape[1]:
        raise ValueError("Input does not have numeric columns.")

    # Normalize the numeric columns using MinMaxScaler
    scaler = MinMaxScaler()
    data[data.select_dtypes(include=[np.number]).columns] = scaler.fit_transform(data[data.select_dtypes(include=[np.number]).columns])

    # Return the normalized data as a pandas DataFrame
    return data
file_name = "data.csv"
data = pd.read_csv(file_name)