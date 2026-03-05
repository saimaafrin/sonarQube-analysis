
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Group the DataFrame by 'id' and apply the scaler to 'Age' and 'Income'
    df[['Age', 'Income']] = df.groupby('id')[['Age', 'Income']].transform(lambda x: scaler.fit_transform(x))
    
    # Calculate the histogram data for the 'Income' column after scaling
    income_hist, income_bins = np.histogram(df['Income'], bins=10, range=(0, 1))
    
    # Return the scaled DataFrame and the histogram data
    return df, income_hist, income_bins