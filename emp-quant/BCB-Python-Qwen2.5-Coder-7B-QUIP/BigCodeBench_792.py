
import heapq
from sklearn.linear_model import LinearRegression

def task_func(df, feature, target, n=10):
    if feature not in df or target not in df:
        raise ValueError("Specified columns are not in the provided DataFrame.")
    
    # Fit the linear regression model
    model = LinearRegression()
    model.fit(df[[feature]], df[target])
    
    # Calculate the residuals
    residuals = df[target] - model.predict(df[[feature]])
    
    # Get the indices of the n largest residuals
    indices = heapq.nlargest(n, range(len(residuals)), abs(residuals))
    
    return indices, model