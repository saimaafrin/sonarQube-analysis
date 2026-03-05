import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    scaler = StandardScaler()
    df_standardized = scaler.fit_transform(df)
    return df_standardized
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})