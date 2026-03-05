import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
def task_func(df, z_threshold=2):
    """
    Identifies and plots outliers in the 'closing_price' column of a given DataFrame using the Z-Score method.
    Constants:
    - Z-Score threshold for identifying outliers is customizable via the 'z_threshold' parameter.
    """
    # Calculate Z-scores
    z_scores = zscore(df['closing_price'])

    # Identify outliers
    outliers = df[np.abs(z_scores) > z_threshold]

    # Plot outliers
    fig, ax = plt.subplots()
    ax.plot(df['closing_price'], label='Closing Prices')
    ax.scatter(outliers['closing_price'], label='Outliers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()

    return outliers, ax