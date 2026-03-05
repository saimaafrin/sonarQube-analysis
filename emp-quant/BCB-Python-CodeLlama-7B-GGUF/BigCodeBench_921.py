
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def normalize_columns(data, columns):
    """
    Normalizes specified columns of a DataFrame using min-max scaling.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame to normalize.
    columns : list of str
        The names of the columns to normalize.

    Returns
    -------
    pandas.DataFrame
        A new DataFrame with the specified columns normalized between 0 and 1.
    """
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data[columns])
    scaled_data = pd.DataFrame(scaled_data, columns=columns)
    return scaled_data