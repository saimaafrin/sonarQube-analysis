import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    """
    Filters rows from the input DataFrame 'df' based on conditions in columns 'B' and 'C', then uses linear regression to predict values in column 'B' using data from column 'A'.
    
    Parameters:
    - df: pandas DataFrame containing the data.
    - col_a: String, the name of the column to be used as the feature (default is 'A').
    - col_b: String, the name of the column to be predicted (default is 'B').
    - col_c: String, the name of the column to be used for filtering (default is 'C').
    - seed: Integer, the random seed for reproducibility of the train-test split (default is None).
    
    Returns:
    - predictions: ndarray, the predicted values for the filtered rows in column 'B', or None if input is invalid.
    - model: LinearRegression, the trained linear regression model, or None if input is invalid.
    """
    # Check if the DataFrame is empty
    if df.empty:
        return None, None
    
    # Check if the specified columns exist in the DataFrame
    if col_a not in df.columns or col_b not in df.columns or col_c not in df.columns:
        return None, None
    
    # Filter the DataFrame based on the conditions
    filtered_df = df[(df[col_b] > 50) & (df[col_c] == 900)]
    
    # Check if the filtered DataFrame is empty
    if filtered_df.empty:
        return None, None
    
    # Check if the columns contain only numeric data
    if not all(pd.api.types.is_numeric_dtype(filtered_df[col_a])) or not all(pd.api.types.is_numeric_dtype(filtered_df[col_b])):
        return None, None
    
    # Split the data into training and testing sets
    X = filtered_df[col_a].values.reshape(-1, 1)
    y = filtered_df[col_b].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)
    
    # Train the LinearRegression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Generate predictions
    predictions = model.predict(X_test)
    
    return predictions, model
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 80, 80, 80, 80], 'C': [900, 900, 900, 900, 900]})