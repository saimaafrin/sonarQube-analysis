from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    # Compute z-scores for numeric columns
    zscores = zscore(df, axis=0, nan_policy='raise')

    # Replace missing values with column means
    zscores = zscores.fillna(zscores.mean())

    # Create a list of histogram axes
    hist_axes = []

    # Plot histograms for each numeric column
    for col in zscores.columns:
        hist_axes.append(plt.hist(zscores[col], bins=10))

    # Return the z-scores DataFrame and the list of histogram axes
    return zscores, hist_axes
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})