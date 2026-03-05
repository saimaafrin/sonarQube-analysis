
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    df_scaled.columns = ['Normalized ' + str(i) for i in df_scaled.columns]
    df_scaled.plot(kind='bar', figsize=(10, 6), title='Normalized Data of ' + df_scaled.columns[0])
    plt.xlabel('Index')
    plt.ylabel('Normalized Value')
    plt.show()
    return df_scaled