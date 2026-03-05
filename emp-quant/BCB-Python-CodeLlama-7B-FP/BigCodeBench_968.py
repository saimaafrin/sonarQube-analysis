import pandas as pd
import seaborn as sns
def task_func(data):
    """
    Creates and returns a heatmap of the cumulative sum of each column in a dictionary.

    Parameters
    ----------
    data : dict
        A dictionary containing the data to be plotted.

    Returns
    -------
    matplotlib.axes._axes.Axes
        The Axes object of the Seaborn heatmap.

    Raises
    ------
    ValueError
        If the DataFrame is empty or if no numeric columns are present.
    """
    # Check if the DataFrame is empty
    if data.empty:
        raise ValueError("The DataFrame is empty.")

    # Check if there are any numeric columns
    numeric_columns = data.select_dtypes(include=[np.number])
    if not numeric_columns.empty:
        raise ValueError("No numeric columns present.")

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    # Compute the cumulative sum of each column
    df_cumsum = df.cumsum()

    # Create a Seaborn heatmap of the cumulative sum
    ax = sns.heatmap(df_cumsum, annot=True, cmap="YlGnBu")

    return ax
data = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}