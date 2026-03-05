
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.exceptions import ValueError

def task_func(data, target, test_size=0.2, random_state=None):
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("Input DataFrame is empty")
    
    # Check if the target column exists in the DataFrame
    if target not in data.columns:
        raise ValueError(f"Target column '{target}' not found in the DataFrame")
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame(data)
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(df, df[target], test_size=test_size, random_state=random_state)
    
    # Initialize and train the RandomForestRegressor
    model = RandomForestRegressor()
    model.fit(X_train, y_train)
    
    # Predict on the test set
    y_pred = model.predict(X_test)
    
    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    
    return mse, model, df