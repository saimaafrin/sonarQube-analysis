import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def task_func(start_date: str, periods: int, freq: str, random_seed: int = 0) -> (pd.DataFrame, plt.Axes):
    """
    Generates and plots a sales forecast starting from a given date, for a specified number of periods and frequency.

    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    
    Parameters:
    - start_date (str): Start date for the forecast in 'YYYY-MM-DD' format.
    - periods (int): Number of periods to forecast.
    - freq (str): Frequency of the forecast (e.g., 'WOM-2FRI' for the second Friday of each month, 'M' for monthly).
    - random_seed (int, optional): Seed for the random number generator to ensure reproducibility.

    Returns:
    - A tuple containing:
        1. A DataFrame with columns ['Date', 'Sales'], where 'Date' is the forecast date and 'Sales' are the forecasted sales.
        2. A matplotlib Axes object for the sales forecast plot.

    Examples:
    >>> df, ax = task_func('2021-01-01', 5, 'WOM-2FRI')
    >>> print(df)
                Sales
    Date             
    2021-01-08    272
    2021-02-12    147
    2021-03-12    217
    2021-04-09    292
    2021-05-14    423
    >>> df, ax = task_func('2022-02-01', 3, 'M', random_seed=42)
    >>> print(df)
                Sales
    Date             
    2022-02-28    202
    2022-03-31    448
    2022-04-30    370
    """
    # Generate a random number for the forecast
    np.random.seed(random_seed)
    forecast = np.random.randint(100, 500, periods)

    # Create a DataFrame with the forecast
    df = pd.DataFrame({'Date': pd.date_range(start=start_date, periods=periods, freq=freq), 'Sales': forecast})

    # Plot the forecast
    ax = df['Sales'].plot(kind='bar', title='Sales forecast', figsize=(10, 5))
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.set_xticks(df['Date'])
    ax.set_xticklabels(df['Date'], rotation=45)
    ax.set_ylim(0, 500)

    return df, ax