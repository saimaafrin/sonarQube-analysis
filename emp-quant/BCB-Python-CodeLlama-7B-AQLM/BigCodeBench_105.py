import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df):
    """
    Perform exploratory data analysis on a dataframe. This function converts the 'date' column to an ordinal format,
    creates a correlation matrix, and generates a pair plot of the dataframe.

    Parameters:
        df (pandas.DataFrame): A dataframe with columns 'group', 'date', and 'value'. The 'date' column should be in datetime format.

    Returns:
        matplotlib.figure.Figure: The figure object for the correlation matrix heatmap.
        seaborn.axisgrid.PairGrid: The PairGrid object for the pair plot.

        The title of the plot is 'Correlation Matrix'. 
    Raises:
        ValueError: If the dataframe is empty, if required columns are missing, or if 'date' column is not in datetime format.

    Requirements:
        - pandas
        - matplotlib.pyplot
        - seaborn

    Example:
        >>> df = pd.DataFrame({
        ...     "group": ["A", "A", "A", "B", "B"],
        ...     "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
        ...     "value": [10, 20, 16, 31, 56],
        ... })
        >>> heatmap_fig, pairplot_grid = task_func(df)
    """
    if df.empty:
        raise ValueError("The dataframe is empty.")
    if "group" not in df.columns:
        raise ValueError("The dataframe is missing the 'group' column.")
    if "date" not in df.columns:
        raise ValueError("The dataframe is missing the 'date' column.")
    if "value" not in df.columns:
        raise ValueError("The dataframe is missing the 'value' column.")
    if not df["date"].dtype == "datetime64[ns]":
        raise ValueError("The 'date' column is not in datetime format.")

    df["date"] = df["date"].dt.to_period("M")

    corr = df.corr()
    corr_fig = plt.figure(figsize=(10, 10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r")
    corr_fig.suptitle("Correlation Matrix")

    pairplot_grid = sns.pairplot(df, hue="group")

    return corr_fig, pairplot_grid