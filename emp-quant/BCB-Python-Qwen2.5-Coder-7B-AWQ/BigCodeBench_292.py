import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Group the DataFrame by 'id' and apply MinMaxScaler to 'Age' and 'Income'
    df[['Age', 'Income']] = df.groupby('id')[['Age', 'Income']].transform(lambda x: scaler.fit_transform(x))
    
    # Create a histogram of the 'Income' column after scaling
    income_histogram = df['Income'].hist(bins=10, grid=False).get_figure()
    
    # Return the scaled DataFrame and the histogram data
    return df, income_histogram