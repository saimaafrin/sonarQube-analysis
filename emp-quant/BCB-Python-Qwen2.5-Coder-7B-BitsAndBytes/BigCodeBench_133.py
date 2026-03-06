
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("DataFrame cannot be empty.")
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the last column
    df.iloc[:, -1] = scaler.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    # Plot the normalized data
    ax = df.iloc[:, -1].plot(kind='line', figsize=(10, 6))
    ax.set_title(f'Normalized Data of {df.columns[-1]}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    return df, ax