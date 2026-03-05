
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df, bins=20):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    last_column = df.columns[-1]
    hist, bins = np.histogram(df[last_column], bins=bins)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of {last_column}')
    return plt.gca()