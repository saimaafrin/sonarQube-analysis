import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
def task_func(data, target, test_size=0.2, random_state=None):
    """
    Trains a RandomForestRegressor model on the input data and returns the mean squared error (MSE) of the predictions and the model.

    Args:
        data (dict): Input data as a dictionary of {feature: value} pairs.
        target (str): Name of the target column in the data.
        test_size (float, optional): Fractional size of the test set. Defaults to 0.2.
        random_state (int, optional): Random seed for reproducibility. Defaults to None.

    Returns:
        float: The mean squared error of the model's predictions on the test set.
        RandomForestRegressor: The trained model.
        DataFrame: The converted dictionary input data.

    Raises:
        ValueError: If the input DataFrame is empty or the target column name is not in the DataFrame.
    """
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Check if the input DataFrame is empty
    if df.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the target column name is in the DataFrame
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in DataFrame")

    # Split the data into a train and test set
    X_train, X_test, y_train, y_test = train_test_split(df.drop(target, axis=1), df[target], test_size=test_size, random_state=random_state)

    # Train a RandomForestRegressor model on the train set
    model = RandomForestRegressor(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error (MSE) of the predictions
    mse = mean_squared_error(y_test, y_pred)

    # Return the MSE, the trained model, and the converted DataFrame
    return mse, model, df
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [6, 7, 8, 9, 10],
    "target": [11, 12, 13, 14, 15]
}