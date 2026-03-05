
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Calculate z-scores for numeric columns
    zscores = zscore(df, axis=0, nan_policy='mean')

    # Create a list of Axes objects to store the histograms
    hist_axes = []

    # Iterate over the numeric columns
    for col in df.select_dtypes(include=['number']).columns:
        # Calculate the histogram for the current column
        hist_axes.append(plt.hist(zscores[col], bins=10))

    # Return the z-scores DataFrame and the list of histogram Axes
    return zscores, hist_axes