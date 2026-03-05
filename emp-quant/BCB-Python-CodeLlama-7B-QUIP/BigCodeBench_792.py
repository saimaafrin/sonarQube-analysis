
import heapq
from sklearn.linear_model import LinearRegression
def task_func(df, feature, target, n=10):
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    model = LinearRegression()
    indices = []
    for i in range(n):
        indices.append(i)
    for i in range(n):
        indices.append(i)
    return indices, model