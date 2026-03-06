
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(file_name: str) -> pd.DataFrame:
    """
    Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as they are.
    """
    # Load the csv file
    df = pd.read_csv(file_name)

    # Get the list of numeric columns
    numeric_columns = [col for col in df.columns if df[col].dtype == 'float64' or df[col].dtype == 'int64']

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Fit the scaler to the numeric columns
    scaler.fit(df[numeric_columns])

    # Transform the data using the scaler
    df[numeric_columns] = scaler.transform(df[numeric_columns])

    # Return the normalized DataFrame
    return df