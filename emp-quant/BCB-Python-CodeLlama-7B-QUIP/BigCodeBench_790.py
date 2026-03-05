
import heapq
from sklearn.preprocessing import StandardScaler
def task_func(df, col1, col2, N=10):
    if col1 not in df or col2 not in df:
        raise ValueError("Specified columns are not in the provided DataFrame")
    scaler = StandardScaler()
    df[col1] = scaler.fit_transform(df[col1].values.reshape(-1, 1))
    df[col2] = scaler.fit_transform(df[col2].values.reshape(-1, 1))
    diffs = df[col1] - df[col2]
    indices = heapq.nlargest(N, range(len(diffs)), diffs.get)
    return indices