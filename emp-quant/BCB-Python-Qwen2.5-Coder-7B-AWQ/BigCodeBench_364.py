import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'
def task_func(df):
    """
    Trains a linear regression model on a given DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing features and target.

    Returns:
    LinearRegression: The trained linear regression model.

    Raises:
    ValueError: If the input is not a DataFrame.
    """
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame.")
    
    # Split the DataFrame into features and target
    X = df[FEATURES]
    y = df[TARGET]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model