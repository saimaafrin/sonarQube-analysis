import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
def task_func(data, columns, target_column):
    """
    Perform a logistic regression on a DataFrame to predict a specific target column.
    
    Parameters:
    - data (pd.DataFrame): The input DataFrame containing the data.
    - columns (list): A list of column names to be used as features for the model.
    - target_column (str): The name of the target column to predict.
    
    Returns:
    - accuracy (float): The accuracy of the logistic regression model.
    """
    # Split the data into features and target
    X = data[columns]
    y = data[target_column]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy