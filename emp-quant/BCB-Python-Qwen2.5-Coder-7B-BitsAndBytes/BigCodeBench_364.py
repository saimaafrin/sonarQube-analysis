
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Constants
FEATURES = ['feature '+str(i) for i in range(1, 11)]
TARGET = 'target'

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Splitting the dataset into features and target variable
    X = df[FEATURES]
    y = df[TARGET]
    
    # Splitting the dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Creating a linear regression model
    model = LinearRegression()
    
    # Training the model
    model.fit(X_train, y_train)
    
    return model