import statistics
import matplotlib.pyplot as plt
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading
    with 'Month' on x-axis and 'Sales' on y-axis.

    Parameters:
    - sales_data (pd.DataFrame): DataFrame with sales data, expected columns: 'Month', 'Product A' to 'Product E'.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object with the sales trends plot.

    Requirements:
    - matplotlib.pyplot
    - statistics

    Example:
    >>> import pandas as pd, numpy as np
    >>> sales_data = pd.DataFrame({
    ...     'Month': range(1, 13),
    ...     'Product A': np.random.randint(100, 200, size=12),
    ...     'Product B': np.random.randint(150, 250, size=12),
    ...     'Product C': np.random.randint(120, 220, size=12),
    ...     'Product D': np.random.randint(130, 230, size=12),
    ...     'Product E': np.random.randint(140, 240, size=12)
    ... })
    >>> ax = task_func(sales_data)
    >>> plt.show()  # Displays the plot
    """
    # TODO: Implement task
    # Hint: Use the following functions:
    # - matplotlib.pyplot.plot
    # - matplotlib.pyplot.fill_between
    # - matplotlib.pyplot.xlabel
    # - matplotlib.pyplot.ylabel
    # - matplotlib.pyplot.title
    # - matplotlib.pyplot.xticks
    # - matplotlib.pyplot.yticks
    # - matplotlib.pyplot.legend
    # - statistics.mean
    # - statistics.stdev
    # - statistics.median
    # - statistics.pstdev
    # - statistics.pvariance
    # - statistics.variance
    # - statistics.median_absolute_deviation
    # - statistics.fmean
    # - statistics.fmedian_mads
    # - statistics.fmedian_low
    # - statistics.fmedian_high
    # - statistics.fmedian_binned
    # - statistics.fmedian_binned_low
    # - statistics.fmedian_binned_high
    # - statistics.fmedian_binned_mads
    # - statistics.fmedian_binned_mad
    # - statistics.fmedian_binned_bin_low
    # - statistics.fmedian_binned_bin_high
    # - statistics.fmedian_binned_bin_mads
    # - statistics.fmedian_binned_bin_mad
    # - statistics.fmedian_binned_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_mad
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_bin_low
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_bin_high
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_bin_bin_bin_mads
    # - statistics.fmedian_binned_bin_bin_bin_bin_bin_bin_bin_