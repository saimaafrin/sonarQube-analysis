
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Scale the 'Age' and 'Income' columns for each group by 'id'
    scaler = MinMaxScaler()
    scaled_df = df[['Age', 'Income']].apply(lambda x: scaler.fit_transform(x))

    # Create a histogram of the scaled 'Income' column
    hist, bin_edges = np.histogram(scaled_df['Income'])

    return (scaled_df, hist)