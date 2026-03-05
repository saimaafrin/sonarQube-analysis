import pandas as pd
import matplotlib.pyplot as plt
def task_func(df):
    """
    Draw and return the daily turnover line chart from a pandas DataFrame.

    Args:
        df (pandas.DataFrame): The DataFrame to draw the chart from.

    Returns:
        matplotlib.axes.Axes: The Matplotlib Axes object with the line chart.

    Raises:
        ValueError: If 'df' is not a DataFrame or lacks 'Date' or 'Sales' columns, or has no data to plot.
    """
    # Check if 'df' is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")

    # Check if 'df' has 'Date' and 'Sales' columns
    if "Date" not in df.columns or "Sales" not in df.columns:
        raise ValueError("'df' must have 'Date' and 'Sales' columns")

    # Check if 'df' has data to plot
    if df.shape[0] == 0:
        raise ValueError("'df' must have data to plot")

    # Draw the line chart
    ax = df.plot(kind="line", x="Date", y="Sales")

    # Return the Matplotlib Axes object
    return ax
df = pd.DataFrame({"Date": ["2022-01-01", "2022-01-02", "2022-01-03"], "Sales": [10, 20, 30]})