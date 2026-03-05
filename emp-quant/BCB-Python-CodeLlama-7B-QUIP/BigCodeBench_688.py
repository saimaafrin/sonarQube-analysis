
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Fit the scaler to the data
    scaler.fit(df)

    # Transform the data
    df_standardized = scaler.transform(df)

    return df_standardized