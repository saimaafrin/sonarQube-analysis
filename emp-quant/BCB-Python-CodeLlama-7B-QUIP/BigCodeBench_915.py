
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the z-scores for each value in the 'closing_price' column
    z_scores = zscore(df['closing_price'])

    # Identify the outliers based on the z-scores and the z-threshold
    outliers = df[abs(z_scores) > z_threshold]

    # Plot the outliers
    fig, ax = plt.subplots()
    ax.plot(outliers['closing_price'])
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    return outliers, fig