import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
def task_func(df, features):
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    return df
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
features = ['A', 'B']