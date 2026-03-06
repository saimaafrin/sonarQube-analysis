import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def task_func(data, columns, target_column):
    """
    Perform a logistic regression on a DataFrame to predict a specific target column.
    
    Parameters:
    - data (numpy.array): The input data as a NumPy array.
    - columns (list): The list of column names.
    - target_column (str): The target column name.

    Returns:
    - accuracy (float): The accuracy of the logistic regression model.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> data = np.random.randint(0, 100, size=(100, 4))  # Using np to generate random data
    >>> columns = ['A', 'B', 'C', 'target']
    >>> task_func(data, columns, 'target')
    0.0
    """
    X = data[:, :-1]
    y = data[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy