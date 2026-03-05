import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
def task_func(df, z_threshold=2):
    """
    Identifies and plots outliers in the 'closing_price' column of a given DataFrame using the Z-Score method.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing the 'closing_price' column.
    z_threshold : float, optional
        The Z-Score threshold for identifying outliers.

    Returns
    -------
    outliers : pandas.DataFrame
        A DataFrame containing the outliers in the 'closing_price' column.
    plot : matplotlib.axes._axes.Axes
        The plot object displaying the outliers, if x-axis label 'Index', y-axis label 'Closing Price', and title 'Outliers in Closing Prices'.
    """
    # Calculate Z-Scores
    z_scores = zscore(df['closing_price'])

    # Identify Outliers
    outliers = df[np.abs(z_scores) > z_threshold]

    # Plot Outliers
    fig, ax = plt.subplots()
    ax.plot(df['closing_price'], label='Closing Prices')
    ax.scatter(outliers['closing_price'], label='Outliers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()

    return outliers, ax
df = pd.DataFrame({'closing_price': [10, 20, 30, 40, 50, 100]})