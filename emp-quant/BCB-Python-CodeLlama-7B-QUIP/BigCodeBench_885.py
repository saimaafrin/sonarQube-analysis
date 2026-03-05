
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def task_func(df, col_a='A', col_b='B', col_c='C', seed=None):
    # Check if input is valid
    if df.empty or df.empty.columns.str.contains('|'.join([col_a, col_b, col_c])):
        return None

    # Filter rows based on conditions in columns 'B' and 'C'
    df_filtered = df.loc[df[col_b] > 50 & df[col_c] == 900]

    # Perform train test split
    X = df_filtered[col_a]
    y = df_filtered[col_b]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

    # Train linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on test set
    predictions = model.predict(X_test)

    return predictions, model