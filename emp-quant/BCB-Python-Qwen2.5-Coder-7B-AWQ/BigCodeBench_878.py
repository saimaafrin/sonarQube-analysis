import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
def task_func(data, target, test_size=0.2, random_state=None):
    """
    Trains a RandomForestRegressor model and returns the mean squared error (MSE) of the predictions and the model.
    
    Parameters:
    - data: A dictionary where keys are feature names and values are lists of feature values.
    - target: The name of the target column in the DataFrame.
    - test_size: The fractional size of the test set.
    - random_state: The seed used by the random number generator.
    
    Returns:
    - float: The mean squared error of the model's predictions on the test set.
    - RandomForestRegressor: The trained model.
    - DataFrame: The converted dictionary input data.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Check if the DataFrame is empty or if the target column is not in the DataFrame
    if df.empty or target not in df.columns:
        raise ValueError("Input DataFrame is empty or the target column name is not in the DataFrame.")
    
    # Split the data into features and target
    X = df.drop(columns=[target])
    y = df[target]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Initialize and train the RandomForestRegressor
    model = RandomForestRegressor(random_state=random_state)
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return mse, model, df