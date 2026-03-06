
import heapq
from sklearn.linear_model import LinearRegression

def task_func(df, feature, target, n=10):
    # Check if the specified columns are in the DataFrame
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame")

    # Fit a simple linear regression model to the two columns
    model = LinearRegression().fit(df[feature], df[target])

    # Get the indices of the n largest residuals
    residuals = model.predict(df[feature]) - df[target]
    indices = heapq.nlargest(n, range(len(residuals)), residuals.take)

    return indices, model