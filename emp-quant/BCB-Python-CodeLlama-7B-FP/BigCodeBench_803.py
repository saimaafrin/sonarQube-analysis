import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(file_name: str) -> pd.DataFrame:
    """
    Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as they are.
    """
    # Load the data
    df = pd.read_csv(file_name)

    # Get the numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns

    # Check if there are any numeric columns
    if not numeric_columns:
        raise ValueError("Input does not have numeric columns.")

    # Normalize the numeric columns
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df
file_name = "data.csv"