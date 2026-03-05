
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

def task_func(data, target, test_size=0.2, random_state=None):
    # Convert data to pandas DataFrame
    data = pd.DataFrame(data)

    # Split data into train and test sets
    train_data, test_data, train_target, test_target = train_test_split(data, target, test_size=test_size, random_state=random_state)

    # Train RandomForestRegressor model
    model = RandomForestRegressor(random_state=random_state)
    model.fit(train_data, train_target)

    # Evaluate model on test set
    test_preds = model.predict(test_data)
    test_mse = mean_squared_error(test_target, test_preds)

    return test_mse, model, data