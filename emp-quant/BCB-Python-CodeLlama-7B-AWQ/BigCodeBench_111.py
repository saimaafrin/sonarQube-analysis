import pandas as pd
import seaborn as sns
def task_func(df):
    """
    Draw and return a heat map with temperature data from a pandas DataFrame.

    Args:
        df (pandas.DataFrame): A DataFrame containing 'Date', 'Time', and 'Temperature' columns.

    Returns:
        sns.heatmap: A Seaborn heatmap object.

    Raises:
        ValueError: If 'df' is not a DataFrame or lacks 'Date', 'Time', or 'Temperature' columns.
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a pandas.DataFrame")
    if not set(["Date", "Time", "Temperature"]).issubset(df.columns):
        raise ValueError("'df' must contain 'Date', 'Time', and 'Temperature' columns")

    # Create a Seaborn heatmap object
    heatmap = sns.heatmap(df.pivot_table(index="Date", columns="Time", values="Temperature"))

    return heatmap
df = pd.DataFrame({"Date": ["2022-01-01", "2022-01-02", "2022-01-03"],
                   "Time": ["08:00", "12:00", "16:00"],
                   "Temperature": [20, 25, 30]})