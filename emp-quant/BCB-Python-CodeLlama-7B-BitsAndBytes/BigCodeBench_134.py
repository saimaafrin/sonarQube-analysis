
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Get the last column of the DataFrame
    last_column = df.columns[-1]

    # Create a histogram of the last column
    hist, bins = np.histogram(df[last_column], bins=bins)

    # Create a Matplotlib Axes object
    fig, ax = plt.subplots()

    # Plot the histogram
    ax.bar(bins[:-1], hist, width=bins[1] - bins[0])

    # Set the title and labels
    ax.set_title(f"Histogram of {last_column}")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    # Return the plot
    return ax.get_figure()