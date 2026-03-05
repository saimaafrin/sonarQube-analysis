import pandas as pd
from sklearn.model_selection import train_test_split
def task_func(df):
    """
    Divide the given DataFrame into a training set and a test set (70%: 30% split), separate the "target" column, and return the four resulting DataFrames.
    """
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
df = pd.DataFrame({"target": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], "feature1": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "feature2": [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]})