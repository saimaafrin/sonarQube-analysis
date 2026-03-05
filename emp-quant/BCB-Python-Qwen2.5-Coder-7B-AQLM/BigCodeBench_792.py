
import heapq
from sklearn.linear_model import LinearRegression

def task_func(df, feature, target, n=10):
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    
    X = df[[feature]]
    y = df[target]
    
    model = LinearRegression()
    model.fit(X, y)
    
    residuals = np.abs(model.predict(X) - y)
    indices = heapq.nlargest(n, range(len(residuals)), residuals.get)
    
    return indices, model