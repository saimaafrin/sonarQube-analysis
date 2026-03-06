
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Scale the 'Age' and 'Income' columns for each group by 'id'
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df[['Age', 'Income']]), columns=['Age', 'Income'])

    # Create a histogram of the scaled 'Income' column
    hist_data = np.histogram(scaled_df['Income'], bins=20)

    return scaled_df, hist_data

scaled_df, hist_data = task_func(df)

print(scaled_df)
print(hist_data)