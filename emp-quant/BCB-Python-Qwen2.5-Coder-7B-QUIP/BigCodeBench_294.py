
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if the required columns are present
    required_columns = ['id', 'age', 'income']
    if not all(column in df for column in required_columns):
        raise ValueError("DataFrame must contain 'id', 'age', and 'income' columns.")

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Standardize the 'age' and 'income' columns
    df['age'] = scaler.fit_transform(df[['age']])
    df['income'] = scaler.fit_transform(df[['income']])

    # Return the standardized DataFrame
    return df