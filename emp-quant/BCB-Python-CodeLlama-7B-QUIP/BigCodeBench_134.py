
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")
    last_column = df.columns[-1]
    hist, bins = np.histogram(df[last_column], bins=bins)
    fig, ax = plt.subplots()
    ax.hist(hist, bins=bins)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {last_column}")
    return ax