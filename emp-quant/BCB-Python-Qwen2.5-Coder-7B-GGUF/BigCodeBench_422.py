
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    """
    Splits the data into train and test datasets after removing a specified column if it exists.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame.
    - target_column (str): The name of the target column.
    - column_to_remove (str): The name of the column to remove from the DataFrame.
    - test_size (float): The proportion of the dataset to include in the test split.
    
    Returns:
    - X_train (pd.DataFrame): Split features for training.
    - X_test (pd.DataFrame): Split features for testing.
    - y_train (pd.Series): Split target values for training.
    - y_test (pd.Series): Split target values for testing.
    """
    # Check if the column to remove exists in the DataFrame
    if column_to_remove in df.columns:
        df = df.drop(columns=[column_to_remove])
    
    # Split the DataFrame into features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    return X_train, X_test, y_train, y_test