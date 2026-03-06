
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the given path
    df = pd.read_csv(data_path)

    # Normalize the dataset using Min-Max Scaler
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)

    # Return the normalized dataset
    return df_scaled