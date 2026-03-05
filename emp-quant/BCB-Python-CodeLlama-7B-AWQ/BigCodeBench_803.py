import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(file_name: str) -> pd.DataFrame:
    """
    Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as they are.
    """
    # Load the data
    df = pd.read_csv(file_name)

    # Check if there are any numeric columns
    if not df.select_dtypes(include=[np.number]).shape[1]:
        raise ValueError("Input does not have numeric columns.")

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Normalize the data
    df_scaled = scaler.fit_transform(df)

    # Return the normalized data
    return df_scaled
file_name = "data.csv"
df = pd.read_csv(file_name)