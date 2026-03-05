import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(df):
    """
    Perform exploratory data analysis on a dataframe.
    This function converts the 'date' column to an ordinal format, creates a correlation matrix, and generates a pair plot of the dataframe.
    The title of the plot is 'Correlation Matrix'.
    The function should raise the exception for:
        ValueError: If the dataframe is empty, if required columns are missing, or if 'date' column is not in datetime format.
    The function should output with:
        matplotlib.figure.Figure: The figure object for the correlation matrix heatmap.
        seaborn.axisgrid.PairGrid: The PairGrid object for the pair plot.
    """
    # Check if the dataframe is empty
    if df.empty:
        raise ValueError("The dataframe is empty.")

    # Check if required columns are missing
    required_columns = ["date", "column1", "column2"]
    if not all(column in df.columns for column in required_columns):
        raise ValueError("Required columns are missing.")

    # Check if 'date' column is in datetime format
    if not pd.to_datetime(df["date"]).is_datetime64:
        raise ValueError("'date' column is not in datetime format.")

    # Convert 'date' column to ordinal format
    df["date"] = pd.to_datetime(df["date"]).dt.to_period("D")

    # Create correlation matrix
    corr = df.corr()

    # Generate pair plot
    sns.set(style="white")
    g = sns.PairGrid(corr, diag_sharey=False)
    g.map_upper(sns.scatterplot)
    g.map_lower(sns.heatmap)
    g.add_legend()

    # Set plot title
    g.fig.suptitle("Correlation Matrix")

    # Return figure and PairGrid objects
    return g.fig, g
df = pd.DataFrame({"date": ["2022-01-01", "2022-01-02", "2022-01-03"],
                   "column1": [1, 2, 3],
                   "column2": [4, 5, 6]})