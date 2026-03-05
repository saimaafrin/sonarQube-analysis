import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(data_path):
    """
    Normalizes a dataset from a .csv file.
    """
    # Load the data from the specified path
    df = pd.read_csv(data_path)

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data using the scaler
    scaled_data = scaler.fit_transform(df)

    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

    return scaled_df
data_path = "data.csv"