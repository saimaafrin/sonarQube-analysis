
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the provided path
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    df_normalized = pd.DataFrame(scaled_data, columns=df.columns)
    
    return df_normalized