
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Check if the DataFrame is empty
    if df.empty:
        return None, None
    
    # Check if the specified columns exist in the DataFrame
    if col_a not in df.columns or col_b not in df.columns or col_c not in df.columns:
        return None, None
    
    # Check if the columns contain only numeric data
    if not (df[col_a].dtype in ['int64', 'float64'] and df[col_b].dtype in ['int64', 'float64'] and df[col_c].dtype in ['int64', 'float64']):
        return None, None
    
    # Filter rows based on conditions
    filtered_df = df[(df[col_b] > 50) & (df[col_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None, None
    
    # Split the data into training and testing sets
    X = filtered_df[col_a].values.reshape(-1, 1)
    y = filtered_df[col_b].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    
    # Train the LinearRegression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Generate predictions for the test set
    predictions = model.predict(X_test)
    
    return predictions, model