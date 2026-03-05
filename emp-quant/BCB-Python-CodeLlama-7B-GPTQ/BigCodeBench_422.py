import pandas as pd
from sklearn.model_selection import train_test_split
def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    """
    Split the data into train and test datasets after removing a specified column if it exists.
    """
    # Check if the column to remove exists
    if column_to_remove in df.columns:
        # Remove the column from the dataframe
        df = df.drop(columns=[column_to_remove])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target_column, axis=1), df[target_column], test_size=test_size)

    # Return the split data
    return X_train, X_test, y_train, y_test
df = pd.DataFrame({"a": [1, 2, 3, 4, 5], "b": [6, 7, 8, 9, 10], "c": [11, 12, 13, 14, 15], "d": [16, 17, 18, 19, 20]})
target_column = "d"
column_to_remove = "c"
test_size = 0.2