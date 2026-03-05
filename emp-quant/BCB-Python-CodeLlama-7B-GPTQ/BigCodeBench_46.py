import pandas as pd
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt
def task_func(df):
    # Calculate z-scores for numeric columns
    zscores = zscore(df.select_dtypes(np.number))

    # Replace missing values with column means
    zscores = zscores.fillna(zscores.mean(axis=0))

    # Draw histograms for each column
    hist_axes = []
    for col in zscores.columns:
        hist_axes.append(plt.hist(zscores[col], bins=10))

    return zscores, hist_axes
df = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                   'B': [6, 7, 8, 9, 10],
                   'C': [11, 12, 13, 14, 15],
                   'D': [16, 17, 18, 19, 20],
                   'E': [21, 22, 23, 24, 25]})