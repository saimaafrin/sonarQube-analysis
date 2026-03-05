
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df):
    # Assuming the DataFrame is named df and the target column is named 'target'
    # First, separate the target column from the rest of the DataFrame
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split the DataFrame into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Return the four resulting DataFrames as a tuple
    return X_train, X_test, y_train, y_test