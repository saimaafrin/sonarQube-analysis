
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    # Remove the specified column if it exists
    if column_to_remove in df:
        df = df.drop(column_to_remove, axis=1)

    # Split the data into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(df, df[target_column], test_size=test_size)

    return X_train, X_test, y_train, y_test