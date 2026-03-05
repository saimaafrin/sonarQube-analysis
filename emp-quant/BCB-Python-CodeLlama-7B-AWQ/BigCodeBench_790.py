import heapq
from sklearn.preprocessing import StandardScaler
import pandas as pd
def task_func(df, col1, col2, N=10):
    """
    Standardize two columns ('col1' and 'col2') in the DataFrame, find the biggest differences between the individual elements of the standardized columns, and return the indices of the N largest differences.
    """
    if col1 not in df.columns or col2 not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")

    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[[col1, col2]])

    diffs = []
    for i in range(N):
        diffs.append(abs(scaled_df[col1][i] - scaled_df[col2][i]))

    return heapq.nlargest(N, diffs)
df = pd.DataFrame({
    'a': [1, 2, 3, 4],
    'b': [1, 2, 3, 5]
})