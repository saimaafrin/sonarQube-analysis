
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Standardize the DataFrame using the StandardScaler from sklearn
    scaler = StandardScaler()
    df_standardized = scaler.fit_transform(df)
    return df_standardized