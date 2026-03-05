import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Standardizes a given DataFrame using the StandardScaler from sklearn.

    Parameters:
    df (DataFrame): The input DataFrame with numeric values.

    Returns:
    DataFrame: The standardized DataFrame.
    """
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized