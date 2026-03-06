
import heapq
from sklearn.preprocessing import StandardScaler

def task_func(df, col1, col2, N=10):
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")

    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[[col1, col2]])

    diffs = []
    for i in range(N):
        diffs.append(abs(scaled_df[i, 0] - scaled_df[i, 1]))

    indices = heapq.nlargest(N, diffs)
    return indices