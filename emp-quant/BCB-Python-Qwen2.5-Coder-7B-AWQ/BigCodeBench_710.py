import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(data_path):
    """
    Normalizes a dataset from a .csv file.

    Parameters:
    data_path (str): The path to the .csv file containing the dataset.

    Returns:
    df (DataFrame): The normalized dataset.
    """
    # Load the dataset from the .csv file
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the dataset
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    return df_normalized