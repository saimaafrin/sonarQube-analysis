
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(df, freq='D', decomposition_model='multiplicative'):
    # Check if 'df' is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")

    # Check if 'df' has the required columns
    if not set(['value']).issubset(df.columns):
        raise ValueError("'df' must have a 'value' column")

    # Check if 'freq' is a valid frequency string
    if freq not in ['D', 'W', 'M']:
        raise ValueError("'freq' must be 'D', 'W', or 'M'")

    # Check if 'decomposition_model' is 'additive' or 'multiplicative'
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError("'decomposition_model' must be 'additive' or 'multiplicative'")

    # Decompose the time series
    decomposition = seasonal_decompose(df['value'], model=decomposition_model, freq=freq)

    # Plot the decomposition results
    fig, ax = plt.subplots()
    ax.plot(decomposition.trend, label='Trend')
    ax.plot(decomposition.seasonal, label='Seasonality')
    ax.plot(decomposition.residuals, label='Residuals')
    ax.legend()
    return (decomposition, ax)