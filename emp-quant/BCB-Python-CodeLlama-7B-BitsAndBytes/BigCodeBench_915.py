
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the Z-scores for each value in the 'closing_price' column
    z_scores = zscore(df['closing_price'])

    # Identify outliers based on the Z-score threshold
    outliers = np.abs(z_scores) > z_threshold

    # Create a new DataFrame containing the outliers
    outliers_df = df[outliers]

    # Plot the outliers
    fig, ax = plt.subplots()
    ax.plot(outliers_df['closing_price'], label='Outliers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()

    return outliers_df, ax