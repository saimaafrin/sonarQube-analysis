import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw and return the daily turnover line chart from a pandas DataFrame.

    Parameters:
    df (DataFrame): A pandas DataFrame with 'Date' and 'Sales' columns.

    Returns:
    Axes: Matplotlib Axes object with the line chart.

    Raises:
    ValueError: If 'df' is not a DataFrame or lacks 'Date' or 'Sales' columns, or has no data to plot.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Example:
    >>> df = pd.DataFrame({
    ...     'Date': pd.date_range(start='1/1/2021', end='12/31/2021'),
    ...     'Sales': np.random.randint(100, 2000, size=365)
    ... })
    >>> ax = task_func(df)
    >>> ax.get_title()  # Expected: 'Daily Turnover'
    'Daily Turnover'
    >>> ax.get_ylabel()  # Expected: 'Sales'
    'Sales'
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('df must be a DataFrame')
    if 'Date' not in df.columns:
        raise ValueError('df must have a column named "Date"')
    if 'Sales' not in df.columns:
        raise ValueError('df must have a column named "Sales"')
    if len(df) == 0:
        raise ValueError('df must have data to plot')

    df = df.copy()
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    df = df.groupby('Date').sum().reset_index()

    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Sales'], color='#0072B2')
    ax.set_title('Daily Turnover')
    ax.set_ylabel('Sales')
    ax.set_xlabel('Date')
    ax.set_xticks(df['Date'])
    ax.set_xticklabels(df['Date'], rotation=45)
    ax.grid(axis='y')
    return ax