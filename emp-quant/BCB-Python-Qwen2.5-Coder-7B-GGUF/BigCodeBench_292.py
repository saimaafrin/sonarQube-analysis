
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Group the DataFrame by 'id' and apply the scaler to 'Age' and 'Income'
    df['Age'] = df.groupby('id')['Age'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten())
    df['Income'] = df.groupby('id')['Income'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)).flatten())
    
    # Extract the histogram data for the 'Income' column
    income_data = df['Income'].values
    income_hist, income_bins = np.histogram(income_data, bins=10)
    
    return df, income_hist, income_bins