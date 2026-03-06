
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, cols):
    """
    Standardize specified numeric columns in a dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe to standardize.
    cols : list
        The list of columns to standardize.

    Returns
    -------
    pandas.DataFrame
        The standardized dataframe.

    Raises
    ------
    ValueError
        If 'df' is not a DataFrame, 'cols' is not a list, or columns in 'cols' don't exist in 'df'.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")
    if not isinstance(cols, list):
        raise ValueError("'cols' must be a list")
    if not all(col in df.columns for col in cols):
        raise ValueError("Columns in 'cols' don't exist in 'df'")

    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled_df, columns=cols, index=df.index)
    return scaled_df