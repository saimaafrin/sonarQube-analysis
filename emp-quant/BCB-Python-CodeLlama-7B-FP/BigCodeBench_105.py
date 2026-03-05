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

    # Check if the required columns are missing
    required_columns = ["date", "value1", "value2"]
    if not all(column in df.columns for column in required_columns):
        raise ValueError("The dataframe is missing required columns.")

    # Check if the 'date' column is in datetime format
    if not df["date"].dtypes == "datetime64[ns]":
        raise ValueError("The 'date' column is not in datetime format.")

    # Convert the 'date' column to an ordinal format
    df["date"] = pd.to_datetime(df["date"]).dt.to_period("D")

    # Create a correlation matrix
    corr_matrix = df.corr()

    # Generate a pair plot of the dataframe
    sns.pairplot(df, diag_kind="kde")

    # Set the title of the plot
    plt.title("Correlation Matrix")

    # Return the figure and PairGrid objects
    return plt.gcf(), sns.PairGrid(df)
df = pd.DataFrame({"date": ["2022-01-01", "2022-01-02", "2022-01-03"],
                   "value1": [1, 2, 3],
                   "value2": [4, 5, 6]})