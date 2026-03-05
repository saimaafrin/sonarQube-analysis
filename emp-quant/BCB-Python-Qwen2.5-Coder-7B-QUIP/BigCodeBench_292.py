
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Initialize the scaler
    scaler = MinMaxScaler()
    
    # Apply scaling to 'Age' and 'Income' columns for each 'id' group
    df['Age'] = df.groupby('id')['Age'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
    df['Income'] = df.groupby('id')['Income'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
    
    # Calculate the histogram data for the 'Income' column
    income_data = df['Income'].values
    income_bins = np.linspace(income_data.min(), income_data.max(), 10)
    income_hist, income_bins = np.histogram(income_data, bins=income_bins)
    
    # Return the scaled DataFrame and the histogram data
    return df, income_hist, income_bins