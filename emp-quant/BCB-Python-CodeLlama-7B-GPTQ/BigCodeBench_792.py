import heapq
from sklearn.linear_model import LinearRegression
def task_func(df, feature, target, n=10):
    """
    Fit a simple linear regression model to two columns of a DataFrame specified by feature and target.
    Return the indices of the n largest residuals as well as the linear regression model.
    """
    if feature not in df.columns or target not in df.columns:
        raise ValueError("Specified columns are not in the provided DataFrame.")

    X = df[feature]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

    residuals = model.predict(X) - y
    indices = heapq.nlargest(n, range(len(residuals)), key=residuals.__getitem__)

    return indices, model
df = pd.DataFrame({
    'a': [1, 2, 3, 4, 5],
    'b': [1, 2, 3, 4, 5]
})