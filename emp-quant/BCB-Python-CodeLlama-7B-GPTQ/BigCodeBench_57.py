import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(csv_file_path: str, title: str):
    """
    Create a heatmap of the correlation matrix of a DataFrame built from a CSV file.
    Round each correlation to 2 decimals.

    Args:
        csv_file_path (str): Path to the CSV file.
        title (str): Title of the plot.

    Returns:
        DataFrame: correlation dataframe where each row and each column correspond to a specific column.
        matplotlib.axes.Axes: The Axes object of the plotted data.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Calculate the correlation matrix
    corr = df.corr()

    # Round each correlation to 2 decimals
    corr = corr.round(2)

    # Create a heatmap of the correlation matrix
    sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, cbar_kws={"ticks": [-1, 0, 1]})

    # Set the title of the plot
    plt.title(title)

    # Return the correlation DataFrame and the Axes object
    return corr, plt.gca()
csv_file_path = "data.csv"
title = "Correlation Matrix"