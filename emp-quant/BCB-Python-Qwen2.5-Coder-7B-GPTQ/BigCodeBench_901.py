import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(d):
    if not d:
        return pd.DataFrame()
    
    # Create a DataFrame from the input list of dictionaries
    df = pd.DataFrame(d)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the DataFrame
    scaled_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled data
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    return scaled_df