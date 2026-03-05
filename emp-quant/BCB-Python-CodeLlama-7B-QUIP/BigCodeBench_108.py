
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def task_func(df, freq='D', decomposition_model='multiplicative'):
    if not isinstance(df, pd.DataFrame):
        raise ValueError('df must be a DataFrame')
    if not set(['value']).issubset(df.columns):
        raise ValueError('df must have a "value" column')
    if not isinstance(freq, str) or freq not in ['D', 'W', 'M']:
        raise ValueError('freq must be a valid frequency string')
    if decomposition_model not in ['additive', 'multiplicative']:
        raise ValueError('decomposition_model must be "additive" or "multiplicative"')

    # Decompose the time series
    decomp = seasonal_decompose(df['value'], freq=freq, decomposition_model=decomposition_model)

    # Create a figure and axis for the plot
    fig, ax = plt.subplots()

    # Plot the trend, seasonality, and residuals
    ax.plot(decomp.trend, label='trend')
    ax.plot(decomp.seasonal, label='seasonality')
    ax.plot(decomp.resid, label='residuals')

    # Set the figure title and labels
    ax.set_title('Time Series Decomposition')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')

    # Return the figure and axis
    return fig, ax