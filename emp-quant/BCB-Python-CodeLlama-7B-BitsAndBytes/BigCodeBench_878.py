
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def task_func(data, target, test_size=0.2, random_state=None):
    # Check if the input DataFrame is empty
    if data.empty:
        raise ValueError("Input DataFrame is empty")

    # Check if the target column name is in the DataFrame
    if target not in data.columns:
        raise ValueError("Target column name is not in the DataFrame")

    # Convert the input data to a pandas DataFrame
    data = pd.DataFrame(data)

    # Split the data into a train and test set
    X_train, X_test, y_train, y_test = train_test_split(data.drop(target, axis=1), data[target], test_size=test_size, random_state=random_state)

    # Train a RandomForestRegressor model on the train set
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Calculate the mean squared error of the predictions
    mse = mean_squared_error(y_test, y_pred)

    # Return the mean squared error and the trained model
    return mse, model, data