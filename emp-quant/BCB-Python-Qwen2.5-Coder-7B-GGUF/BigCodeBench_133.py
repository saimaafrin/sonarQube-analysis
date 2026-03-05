
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    scaler = MinMaxScaler()
    df.iloc[:, -1] = scaler.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df.iloc[:, -1], marker='o', linestyle='-', color='b')
    plt.title(f'Normalized Data of {df.columns[-1]}')
    plt.xlabel('Index')
    plt.ylabel('Normalized Value')
    plt.grid(True)
    plt.show()
    
    return df, plt.gca()