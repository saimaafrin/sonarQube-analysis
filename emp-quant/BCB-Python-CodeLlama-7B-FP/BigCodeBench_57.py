import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(csv_file_path: str, title: str):
    """
    Create a heatmap of the correlation matrix of a DataFrame built from a CSV file.
    Round each correlation to 2 decimals.

    Args:
        csv_file_path (str): Path to the CSV file.
        title (str): Title of the heatmap.

    Returns:
        DataFrame: correlation dataframe where each row and each column correspond to a specific column.
        matplotlib.axes.Axes: The Axes object of the plotted data.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)

    # Calculate the correlation matrix
    corr = df.corr()

    # Round each correlation to 2 decimals
    corr = corr.round(2)

    # Create a heatmap of the correlation matrix
    sns.heatmap(corr, annot=True, cmap="coolwarm", xticklabels=corr.columns, yticklabels=corr.columns)

    # Set the title of the heatmap
    plt.title(title)

    # Return the correlation DataFrame and the Axes object of the plotted data
    return corr, plt.gca()
csv_file_path = "data.csv"
title = "Correlation Matrix"