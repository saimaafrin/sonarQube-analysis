import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(df, features):
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10]})
features = ['A', 'B']