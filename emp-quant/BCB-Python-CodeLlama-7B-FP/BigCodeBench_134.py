import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, bins=20):
    """
    Draw a histogram of the last column of the DataFrame and return the plot.
    The function should raise the exception for:
        ValueError: If the input is not a DataFrame, or if the DataFrame is empty.
    The function should output with:
        Axes: A Matplotlib Axes object representing the histogram of the last column.
        Title: 'Histogram of ' followed by the name of the last column.
        X-axis label: 'Value'
        Y-axis label: 'Frequency'
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")
    last_column = df.columns[-1]
    hist = df[last_column].hist(bins=bins)
    hist.set_title(f"Histogram of {last_column}")
    hist.set_xlabel("Value")
    hist.set_ylabel("Frequency")
    return hist
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})