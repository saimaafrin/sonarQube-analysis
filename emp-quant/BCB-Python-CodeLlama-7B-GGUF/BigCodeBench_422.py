
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    # Check if the specified column exists in the dataframe
    if column_to_remove not in df.columns:
        raise ValueError(f"Column {column_to_remove} does not exist in the dataframe")

    # Remove the specified column from the dataframe
    df.drop(columns=column_to_remove, inplace=True)

    # Split the dataframe into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=test_size)

    return X_train, X_test, y_train, y_test