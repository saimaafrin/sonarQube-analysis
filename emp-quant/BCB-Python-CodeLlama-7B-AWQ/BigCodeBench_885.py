import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    """
    This function filters rows from the input DataFrame 'df' based on conditions in columns 'B' and 'C', then uses linear regression to predict values in column 'B' using data from column 'A'. Specifically, it selects rows where column 'B' values are greater than 50 and column 'C' values equal 900. A train test split of the remaining data is performed, where the test_size = 0.2 and col_a is used as X value and col_b is used as Y values / target. This data is used to train a LinearRegression model. The test split is used to generate predictions for col_b. These predictions are returned as well as the trained model. If df is empty or empty after the filtering, None is returned. If df does contain non numeric data None is returned. If the specified columns are not contained in df, None is returned.
    """
    # Check if the input DataFrame is empty or contains non numeric data
    if df.empty or df.select_dtypes(include=[np.number]).empty:
        return None

    # Check if the specified columns are not contained in df
    if col_a not in df.columns or col_b not in df.columns or col_c not in df.columns:
        return None

    # Filter rows based on conditions in columns 'B' and 'C'
    df_filtered = df[(df[col_b] > 50) & (df[col_c] == 900)]

    # If the filtered DataFrame is empty, return None
    if df_filtered.empty:
        return None

    # Split the data into training and testing sets
    X = df_filtered[col_a]
    y = df_filtered[col_b]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

    # Train a LinearRegression model on the training data
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Use the trained model to make predictions on the testing data
    y_pred = model.predict(X_test)

    # Return the predictions and the trained model
    return y_pred, model
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 80, 80, 80, 80], 'C': [900, 900, 900, 900, 900]})