
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Compute z-scores for each numeric column
    zscores = df.apply(zscore)

    # Replace missing values with column average
    zscores = zscores.fillna(zscores.mean())

    # Create a histogram for each numeric column
    hist_axes = []
    for col in zscores.columns:
        hist_axes.append(plt.hist(zscores[col], bins=10))

    # Return the z-scores DataFrame and the list of histogram Axes objects
    return zscores, hist_axes