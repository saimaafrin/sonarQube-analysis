import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
def task_func(df, freq='D', decomposition_model='multiplicative'):
    """
    Decomposes a time series in the 'value' column of a DataFrame into trend, seasonality, and residuals.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing the time series data.
    freq (str, optional): The frequency of the time series. Defaults to 'D' (daily).
    decomposition_model (str, optional): The decomposition model to use. Defaults to 'multiplicative'.

    Returns:
    tuple: A tuple containing the decomposition result (DecomposeResult object) and the matplotlib Axes object.

    Raises:
    ValueError: If 'df' is not a DataFrame, lacks required columns, or contains invalid data types.
    ValueError: If 'freq' is not a valid frequency string.
    ValueError: If 'decomposition_model' is not 'additive' or 'multiplicative'.
    """
    # Check if df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")

    # Check if df has required columns
    if 'value' not in df.columns:
        raise ValueError("'df' must have a 'value' column")

    # Check if df contains invalid data types
    if not all(isinstance(x, (int, float)) for x in df['value']):
        raise ValueError("'df' must contain only integers or floats in the 'value' column")

    # Check if freq is a valid frequency string
    if freq not in ['D', 'W', 'M']:
        raise ValueError("'freq' must be 'D' (daily), 'W' (weekly), or 'M' (monthly)")

    # Check if decomposition_model is 'additive' or 'multiplicative'
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("'decomposition_model' must be 'additive' or 'multiplicative'")

    # Decompose the time series
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, freq=freq)

    # Plot the decomposition results
    fig, ax = plt.subplots()
    ax.plot(decomposition.trend, label='Trend')
    ax.plot(decomposition.seasonal, label='Seasonality')
    ax.plot(decomposition.resid, label='Residuals')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()

    return (decomposition, ax)
df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})