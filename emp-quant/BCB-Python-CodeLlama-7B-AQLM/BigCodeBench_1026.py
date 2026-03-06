import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
def task_func(kwargs):
    """
    Performs a two-sample t-test on numerical data from two groups to determine if there is a significant
    difference in their means. The function handles NaN values, computes descriptive statistics for each group,
    and generates a boxplot and histograms for data visualization.

    Parameters:
    - kwargs (dict): A dictionary with two keys, 'group1' and 'group2'. Each key maps to a list of numbers.
                     Lists can contain NaN values, which will be excluded from analysis.

    Returns:
    - dict: A dictionary containing:
        - 'significant': Boolean. True if the means of the two groups are significantly different (p < 0.05).
        - 'group1_stats': Dictionary with mean and standard deviation of 'group1' (excluding NaNs).
        - 'group2_stats': Dictionary with mean and standard deviation of 'group2' (excluding NaNs).
        - 'ax_boxplot': A matplotlib Axes object with a boxplot comparing 'group1' and 'group2'.
        - 'ax_histogram': A matplotlib Axes object with histograms of 'group1' and 'group2'.

    Raises:
    - ValueError: If either group is empty, contains only NaN values, has less than two non-NaN values,
                  or if the variance in one or both groups is below a threshold (1e-8).

    Requirements:
    - numpy
    - scipy
    - matplotlib

    Note:
    - The function sets the significance level (alpha) at 0.05.
    - It removes NaN values before performing any calculations or plotting.
    - A t-test is performed with the 'nan_policy' set to 'omit' to ignore NaNs.
    - The function checks for sufficient non-NaN data points and adequate variance in each group before conducting the t-test.
    - The boxplot and histograms provide a visual comparison of the data distributions.
    
    Example:
    >>> data = {'group1': [1, 2, 3, 4], 'group2': [5, 6, 7, 8]}
    >>> results = task_func(data)
    >>> results['significant']
    True
    """
    # Check if the groups are empty or contain NaN values
    if not kwargs['group1'] or not kwargs['group2']:
        raise ValueError('One or both groups are empty or contain NaN values.')

    # Check if the groups have less than two non-NaN values
    if len(kwargs['group1']) < 2 or len(kwargs['group2']) < 2:
        raise ValueError('One or both groups have less than two non-NaN values.')

    # Check if the variance in one or both groups is below a threshold
    if np.var(kwargs['group1']) < 1e-8 or np.var(kwargs['group2']) < 1e-8:
        raise ValueError('One or both groups have a variance below 1e-8.')

    # Remove NaN values from each group
    group1 = [x for x in kwargs['group1'] if not np.isnan(x)]
    group2 = [x for x in kwargs['group2'] if not np.isnan(x)]

    # Compute descriptive statistics for each group
    group1_stats = {'mean': np.mean(group1), 'std': np.std(group1)}
    group2_stats = {'mean': np.mean(group2), 'std': np.std(group2)}

    # Perform a two-sample t-test
    t_stat, p_val = ttest_ind(group1, group2, nan_policy='omit')

    # Generate a boxplot and histograms for data visualization
    fig, (ax_boxplot, ax_histogram) = plt.subplots(1, 2, figsize=(12, 6))
    ax_boxplot.boxplot([group1, group2], labels=['group1', 'group2'])
    ax_histogram.hist(group1, label='group1')
    ax_histogram.hist(group2, label='group2')
    ax_histogram.legend()

    # Return results
    return {'significant': p_val < 0.05, 'group1_stats': group1_stats, 'group2_stats': group2_stats,
            'ax_boxplot': ax_boxplot, 'ax_histogram': ax_histogram}