import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Standardize a DataFrame using StandardScaler from sklearn.

    Parameters:
    df (DataFrame): The input DataFrame with numeric values.

    Returns:
    df_standardized (DataFrame): The standardized DataFrame.
    """
    scaler = StandardScaler()
    df_standardized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
    return df_standardized