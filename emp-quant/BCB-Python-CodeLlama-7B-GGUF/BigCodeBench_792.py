
import heapq
from sklearn.linear_model import LinearRegression

def task_func(df, feature, target, n=10):
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")

    X = df[feature]
    y = df[target]

    model = LinearRegression().fit(X, y)

    residuals = model.residuals_
    indices = heapq.nlargest(n, range(len(residuals)), residuals.__getitem__)

    return indices, model