
import heapq
from sklearn.linear_model import LinearRegression

def task_func(df, feature, target, n=10):
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    
    X = df[[feature]]
    y = df[target]
    
    model = LinearRegression()
    model.fit(X, y)
    
    residuals = abs(y - model.predict(X))
    largest_residual_indices = heapq.nlargest(n, range(len(residuals)), residuals.get)
    
    return largest_residual_indices, model