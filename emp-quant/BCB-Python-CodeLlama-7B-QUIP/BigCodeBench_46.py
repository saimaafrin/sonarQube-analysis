
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(df):
    # Calculate z-scores for each numeric column
    zscores = zscore(df, axis=0)

    # Replace missing values with the column's average
    zscores = zscores.fillna(zscores.mean())

    # Create histograms for each numeric column
    fig, axs = plt.subplots(nrows=zscores.shape[1], ncols=1, figsize=(10, 10))
    for i, col in enumerate(zscores.columns):
        axs[i].hist(zscores[col], bins=10)

    # Return the DataFrame with z-scores and the list of Axes objects
    return zscores, axs