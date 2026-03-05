
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the cumulative sum for each column in a given DataFrame and plot the results in a bar chart.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to calculate the cumulative sum for.

    Returns
    -------
    tuple
        A tuple containing:

        (1) A DataFrame with cumulative sums for each column.
        (2) A matplotlib bar chart Figure of these cumulative sums.

    Raises
    ------
    ValueError
        If the DataFrame is empty or contains non-numeric data.
    """
    if df.empty or not df.select_dtypes(include=[np.number]).empty:
        raise ValueError("The DataFrame is empty or contains non-numeric data.")

    # Calculate the cumulative sum for each column
    cumulative_sums = df.apply(lambda x: x.cumsum(), axis=0)

    # Create a bar chart Figure
    fig, ax = plt.subplots()
    ax.bar(cumulative_sums.index, cumulative_sums.values)
    ax.set_title("Cumulative Sum per Column")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.legend()

    return cumulative_sums, fig