import pandas as pd
import matplotlib.pyplot as plt
def task_func(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate the cumulative sum for each column in a given DataFrame and plot the results in a bar chart.
    NaN values are ignored in the cumulative sum calculation, i.e. treated as zero for the purpose of the sum without changing existing values to NaN.
    The plot title is set to 'Cumulative Sum per Column'. X-axis label is 'Index' and Y-axis label is 'Cumulative Sum'. A legend is included in the plot.
    The function should raise the exception for: ValueError: If the DataFrame is empty or contains non-numeric data.
    The function should output with:
        tuple: A tuple containing:
        (1) A DataFrame with cumulative sums for each column.
        (2) A matplotlib bar chart Figure of these cumulative sums.
    """
    # Check if the DataFrame is empty or contains non-numeric data
    if df.empty or not df.apply(lambda x: x.dtype in [np.number, np.bool]).all():
        raise ValueError("The DataFrame is empty or contains non-numeric data.")

    # Calculate the cumulative sum for each column
    cumulative_sum = df.apply(lambda x: x.cumsum(skipna=True))

    # Create a bar chart Figure
    fig, ax = plt.subplots()
    ax.bar(cumulative_sum.index, cumulative_sum.values)
    ax.set_title("Cumulative Sum per Column")
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.legend()

    # Return the DataFrame and the bar chart Figure
    return cumulative_sum, fig
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]})