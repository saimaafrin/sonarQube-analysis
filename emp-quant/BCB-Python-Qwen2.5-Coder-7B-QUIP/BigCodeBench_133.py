
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame")
    
    scaler = MinMaxScaler()
    df.iloc[:, -1] = scaler.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))
    
    plt.figure()
    plt.plot(df.index, df.iloc[:, -1], label='Normalized Data')
    plt.title(f'Normalized Data of {df.columns[-1]}')
    plt.xlabel('Index')
    plt.ylabel('Normalized Value')
    plt.legend()
    
    return df, plt.gca()