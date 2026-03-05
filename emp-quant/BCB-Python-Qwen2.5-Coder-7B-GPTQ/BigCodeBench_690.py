import pandas as pd
from sklearn.linear_model import LinearRegression
COLUMNS = ['X', 'Y']
def task_func(df):
    """
    Fits a linear regression model to the given DataFrame.

    Parameters:
    df (pd.DataFrame): A DataFrame with columns 'X' and 'Y' containing numeric values.

    Returns:
    model (LinearRegression): The fitted linear regression model.
    """
    # Ensure the DataFrame has the correct columns
    if not all(col in df.columns for col in COLUMNS):
        raise ValueError("DataFrame must contain columns 'X' and 'Y'")

    # Extract features and target variable
    X = df['X'].values.reshape(-1, 1)
    y = df['Y'].values

    # Initialize and fit the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    return model