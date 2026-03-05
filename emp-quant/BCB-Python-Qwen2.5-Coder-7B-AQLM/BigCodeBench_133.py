
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    scaler = MinMaxScaler()
    df.iloc[:, -1] = scaler.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    column_name = df.columns[-1]
    fig, ax = plt.subplots()
    ax.plot(df.index, df[column_name], marker='o')
    ax.set_title(f'Normalized Data of {column_name}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    return df, ax