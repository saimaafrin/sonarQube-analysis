import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
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
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")

    # Check if required columns are present
    if 'value' not in df.columns:
        raise ValueError("'df' must have a 'value' column")

    # Check if data types are valid
    if not all(isinstance(x, (int, float)) for x in df['value']):
        raise ValueError("'df' must contain only integers or floats in 'value' column")

    # Check if frequency is valid
    if freq not in ['D', 'W', 'M', 'Q', 'A']:
        raise ValueError("'freq' must be a valid frequency string")

    # Check if decomposition model is valid
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("'decomposition_model' must be 'additive' or 'multiplicative'")

    # Decompose the time series
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, freq=freq)

    # Plot the decomposition
    fig, ax = plt.subplots()
    decomposition.plot(ax=ax)

    return (decomposition, ax)
df = pd.DataFrame({'value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
freq = 'D'
decomposition_model = 'multiplicative'