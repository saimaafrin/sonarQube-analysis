
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame) -> tuple:
    # Check if the DataFrame is empty or contains non-numeric data
    if df.empty or df.isnull().any().any():
        raise ValueError("The DataFrame is empty or contains non-numeric data")

    # Calculate the cumulative sum for each column
    cumsums = df.apply(lambda x: x.cumsum())

    # Create a bar chart of the cumulative sums
    fig, ax = plt.subplots()
    ax.bar(cumsums.index, cumsums.values, label=cumsums.index)
    ax.set_xlabel("Index")
    ax.set_ylabel("Cumulative Sum")
    ax.set_title("Cumulative Sum per Column")
    ax.legend()

    return cumsums, fig