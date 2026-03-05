import pandas as pd
import matplotlib.pyplot as plt
def task_func(df, bins=20):
    """
    Draw a histogram of the last column of the DataFrame and return the plot.

    Args:
        df (pandas.DataFrame): The DataFrame to draw the histogram from.
        bins (int, optional): The number of bins to use for the histogram. Defaults to 20.

    Returns:
        matplotlib.axes.Axes: A Matplotlib Axes object representing the histogram of the last column.

    Raises:
        ValueError: If the input is not a DataFrame, or if the DataFrame is empty.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas.DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Get the last column of the DataFrame
    col = df.columns[-1]

    # Draw the histogram
    ax = df[col].hist(bins=bins, alpha=0.5, label=col)

    # Set the title and labels
    ax.set_title(f"Histogram of {col}")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})