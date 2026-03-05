import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Group the DataFrame by 'id' and apply MinMaxScaler to 'Age' and 'Income' columns
    df['Age'] = df.groupby('id')['Age'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
    df['Income'] = df.groupby('id')['Income'].transform(lambda x: scaler.fit_transform(x.values.reshape(-1, 1)))
    
    # Extract the histogram data for the 'Income' column after scaling
    income_data = df['Income'].values.flatten()
    hist, bin_edges = np.histogram(income_data, bins=10)
    
    # Return the scaled DataFrame and the histogram data
    return df, (hist, bin_edges)