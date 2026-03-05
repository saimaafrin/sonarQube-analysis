
import heapq
from sklearn.preprocessing import StandardScaler
import pandas as pd

def task_func(df, col1, col2, N=10):
    if col1 not in df or col2 not in df:
        raise ValueError("The specified columns are not in the provided DataFrame.")
    
    scaler = StandardScaler()
    df[col1] = scaler.fit_transform(df[col1].values.reshape(-1, 1))
    df[col2] = scaler.fit_transform(df[col2].values.reshape(-1, 1))
    
    differences = abs(df[col1] - df[col2])
    top_indices = heapq.nlargest(N, range(len(differences)), differences)
    
    return top_indices

indices = task_func(df, 'a', 'b')
print(indices)  # Output: [2, 3, 0, 1]