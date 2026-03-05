
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df):
    # Split the DataFrame into a training set and a test set
    X_train, X_test, y_train, y_test = train_test_split(df, df["target"], test_size=0.3, random_state=42)
    return (X_train, X_test, y_train, y_test)