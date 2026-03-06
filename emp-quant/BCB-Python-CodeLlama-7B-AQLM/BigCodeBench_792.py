import heapq
from sklearn.linear_model import LinearRegression
def task_func(df, feature, target, n=10):
    """
    Fit a simple linear regression model to two columns of a DataFrame 
    specified by feature and target. 
    return the indices of the n largest residuals as well as the linear 
    regression model.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame with at least two numerical columns named 'col1' and 'col2'.
    feature (str): The DataFrame column used as feature.
    target (str): The DataFrame column used as target.
    n (int, optional): Number of largest residuals to return. Default is 10.
    
    Returns:
    list[int]: Indices of the n largest residuals.
    LinearRegression: The LinearRegression model.
    
    Raises:
    ValueError: If specified columns are not in the provided DataFrame.

    Requirements:
    - heapq
    - sklearn.linear_model
    
    Example:
    >>> df = pd.DataFrame({
    ...     'col1': [99, 86, 90, 70, 86, 95, 56, 98, 80, 81],
    ...     'col2': [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
    ... })
    >>> indices, model = task_func(df, 'col1', 'col2', n=5)
    >>> print(indices)
    [0, 1, 9, 7, 8]
    >>> print(model)
    LinearRegression()

    >>> df = pd.DataFrame({
    ...     'a': [1, 2, 3, 4, 5],
    ...     'b': [1, 2, 3, 4, 5]
    ... })
    >>> indices, model = task_func(df, 'a', 'b', n=3)
    >>> print(indices)
    [0, 1, 2]
    >>> print(model)
    LinearRegression()
    """
    if feature not in df.columns:
        raise ValueError(f"'{feature}' is not a column in the DataFrame.")
    if target not in df.columns:
        raise ValueError(f"'{target}' is not a column in the DataFrame.")
    if len(df) < 2:
        raise ValueError("The DataFrame must contain at least two rows.")
    if len(df[feature]) != len(df[target]):
        raise ValueError("The DataFrame must contain the same number of rows for both columns.")
    if len(df[feature]) < 2:
        raise ValueError("The DataFrame must contain at least two rows.")
    if len(df[feature]) < n:
        raise ValueError("The DataFrame must contain at least n rows.")

    # fit the model
    model = LinearRegression()
    model.fit(df[feature].values.reshape(-1, 1), df[target].values.reshape(-1, 1))

    # get the residuals
    residuals = model.predict(df[feature].values.reshape(-1, 1)) - df[target].values.reshape(-1, 1)

    # get the indices of the n largest residuals
    indices = []
    for i in range(n):
        indices.append(heapq.nlargest(len(residuals), range(len(residuals)), residuals.__getitem__)[i])

    return indices, model