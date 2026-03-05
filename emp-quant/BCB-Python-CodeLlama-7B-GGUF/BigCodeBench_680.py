
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def task_func(df, features):
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[features])
    df[features] = scaled_features
    return df