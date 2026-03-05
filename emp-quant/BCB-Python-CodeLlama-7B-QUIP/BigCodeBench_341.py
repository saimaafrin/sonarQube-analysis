
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, col):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if not df.columns.contains(col):
        raise ValueError("DataFrame must contain the specified column")
    if not df[col].dtype == "float64":
        raise ValueError("Column must be numerical")

    # Create subplots
    fig, axs = plt.subplots(nrows=2, ncols=1, sharex=True)

    # Plot histogram
    axs[0].hist(df[col], bins=50, density=True)
    axs[0].set_xlabel("Value")
    axs[0].set_ylabel("Density")

    # Plot box plot
    axs[1].boxplot(df[col])
    axs[1].set_xlabel("Value")
    axs[1].set_ylabel("Box plot")

    # Return figure
    return fig