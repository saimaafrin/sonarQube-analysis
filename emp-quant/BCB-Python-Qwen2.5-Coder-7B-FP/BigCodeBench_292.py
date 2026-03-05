import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Group the DataFrame by 'id' and apply MinMaxScaler to 'Age' and 'Income'
    df[['Age', 'Income']] = df.groupby('id')[['Age', 'Income']].transform(lambda x: scaler.fit_transform(x))
    
    # Calculate the histogram data for the 'Income' column
    income_hist, income_bins = np.histogram(df['Income'], bins=10)
    
    # Return the scaled DataFrame and the histogram data
    return df, income_hist, income_bins