import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values, standardize it with the standard scaler from sklearn.
    The function should output with:
        df_standardized (DataFrame): The standardized DataFrame.
    """
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Fit the scaler to the DataFrame
    scaler.fit(df)

    # Transform the DataFrame using the scaler
    df_standardized = scaler.transform(df)

    return df_standardized
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})