
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    # Scale the 'Age' and 'Income' columns for each group by 'id'
    scaler = MinMaxScaler()
    scaled_df = pd.DataFrame(scaler.fit_transform(df[['Age', 'Income']]), columns=['Age', 'Income'])

    # Create a histogram of the 'Income' column after scaling
    income_hist = np.histogram(scaled_df['Income'], bins=50)

    return scaled_df, income_hist

print(scaled_df)
print(income_hist)