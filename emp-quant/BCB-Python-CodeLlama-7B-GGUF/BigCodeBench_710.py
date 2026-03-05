
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_data(data_path):
    """
    Normalizes a dataset from a .csv file.

    Args:
        data_path (str): Path to the .csv file containing the dataset.

    Returns:
        df (DataFrame): The normalized dataset.
    """
    df = pd.read_csv(data_path)
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled