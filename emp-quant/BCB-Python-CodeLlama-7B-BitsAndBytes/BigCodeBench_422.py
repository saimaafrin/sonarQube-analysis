
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    # Check if the column to remove exists in the DataFrame
    if column_to_remove in df.columns:
        # Remove the column from the DataFrame
        df = df.drop(columns=[column_to_remove])

    # Split the DataFrame into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df, df[target_column], test_size=test_size)

    # Return the split DataFrames and Series
    return X_train, X_test, y_train, y_test

X_train, X_test, y_train, y_test = task_func(df, target_column, column_to_remove, test_size)
print(X_train)
print(X_test)
print(y_train)
print(y_test)