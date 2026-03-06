
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Check if the required columns exist in the DataFrame
    if col_a not in df.columns or col_b not in df.columns or col_c not in df.columns:
        return None
    
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[col_b] > 50) & (df[col_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None
    
    # Check if all columns contain numeric data
    if not all(filtered_df[col_a].apply(pd.api.types.is_numeric_dtype)) or \
       not all(filtered_df[col_b].apply(pd.api.types.is_numeric_dtype)):
        return None
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        filtered_df[col_a], filtered_df[col_b], test_size=0.2, random_state=seed)
    
    # Train the Linear Regression model
    model = LinearRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)
    
    # Generate predictions on the test set
    predictions = model.predict(X_test.values.reshape(-1, 1))
    
    return predictions, model