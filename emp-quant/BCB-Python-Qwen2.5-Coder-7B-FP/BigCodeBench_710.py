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
    
    # Fit and transform the dataset
    df_scaled = scaler.fit_transform(df)
    
    # Convert the scaled data back to a DataFrame
    df = pd.DataFrame(df_scaled, columns=df.columns)
    
    return df