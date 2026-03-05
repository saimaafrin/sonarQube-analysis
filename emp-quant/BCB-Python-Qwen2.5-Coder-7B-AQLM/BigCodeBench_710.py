
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    # Load the dataset from the .csv file
    df = pd.read_csv(data_path)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    df_scaled = scaler.fit_transform(df)
    
    # Convert the scaled data back to a DataFrame
    df = pd.DataFrame(df_scaled, columns=df.columns)
    
    return df