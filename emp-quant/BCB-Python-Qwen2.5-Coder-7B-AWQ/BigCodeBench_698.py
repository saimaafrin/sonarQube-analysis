import pandas as pd
from sklearn.model_selection import train_test_split
def task_func(df):
    """
    Splits the given DataFrame into training and test sets (70:30 split),
    separates the 'target' column, and returns the four resulting DataFrames.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the data.

    Returns:
    tuple: A tuple containing four DataFrames: X_train, X_test, y_train, y_test.
    """
    # Separate the target column
    X = df.drop(columns=['target'])
    y = df['target']
    
    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test