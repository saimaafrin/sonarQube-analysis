
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the .csv file
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the dataset
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    
    return df_normalized