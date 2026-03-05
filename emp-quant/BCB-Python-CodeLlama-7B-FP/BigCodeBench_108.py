import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import pytest
def task_func(df, freq='D', decomposition_model='multiplicative'):
    """
    Decomposes a time series in the 'value' column of a DataFrame into trend, seasonality, and residuals.

    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame.
    freq : str, optional
        The frequency of the time series.
    decomposition_model : str, optional
        The decomposition model to use.

    Returns
    -------
    tuple
        A tuple containing the decomposition result (DecomposeResult object) and the matplotlib Axes object.

    Raises
    ------
    ValueError
        If 'df' is not a DataFrame, lacks required columns, or contains invalid data types.
    ValueError
        If 'freq' is not a valid frequency string.
    ValueError
        If 'decomposition_model' is not 'additive' or 'multiplicative'.
    """
    # Check input data
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")
    if 'value' not in df.columns:
        raise ValueError("'df' must have a 'value' column")
    if not isinstance(freq, str):
        raise ValueError("'freq' must be a string")
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("'decomposition_model' must be 'additive' or 'multiplicative'")

    # Decompose time series
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, freq=freq)

    # Plot decomposition
    fig, ax = plt.subplots()
    decomposition.plot(ax=ax)
    ax.set_title('Time Series Decomposition')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    return (decomposition, ax)