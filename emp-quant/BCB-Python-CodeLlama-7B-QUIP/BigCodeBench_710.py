
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset
    df = pd.read_csv(data_path)

    # Normalize the dataset
    scaler = MinMaxScaler()
    df_normalized = scaler.fit_transform(df)

    return df_normalized