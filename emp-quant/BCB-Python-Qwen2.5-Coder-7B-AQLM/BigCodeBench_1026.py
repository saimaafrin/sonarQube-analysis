
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

def task_func(kwargs):
    group1 = kwargs.get('group1', [])
    group2 = kwargs.get('group2', [])
    
    # Check for empty or all NaN groups
    if not group1 or not group2:
        raise ValueError("Groups cannot be empty.")
    if all(np.isnan(group1)) or all(np.isnan(group2)):
        raise ValueError("Groups cannot contain only NaN values.")
    
    # Remove NaN values
    group1 = np.array(group1, dtype=float)
    group2 = np.array(group2, dtype=float)
    group1 = group1[~np.isnan(group1)]
    group2 = group2[~np.isnan(group2)]
    
    # Check for sufficient non-NaN data points
    if len(group1) < 2 or len(group2) < 2:
        raise ValueError("Groups must contain at least two non-NaN values.")
    
    # Check for adequate variance
    if np.var(group1) < 1e-8 or np.var(group2) < 1e-8:
        raise ValueError("Groups must have adequate variance.")
    
    # Perform t-test
    t_stat, p_value = ttest_ind(group1, group2, nan_policy='omit')
    
    # Determine significance
    significant = p_value < 0.05
    
    # Compute descriptive statistics
    group1_stats = {'mean': np.mean(group1), 'std': np.std(group1)}
    group2_stats = {'mean': np.mean(group2), 'std': np.std(group2)}
    
    # Create boxplot
    fig, ax_boxplot = plt.subplots()
    ax_boxplot.boxplot([group1, group2], labels=['Group 1', 'Group 2'])
    
    # Create histograms
    fig, ax_histogram = plt.subplots()
    ax_histogram.hist(group1, bins=10, alpha=0.5, label='Group 1')
    ax_histogram.hist(group2, bins=10, alpha=0.5, label='Group 2')
    ax_histogram.legend()
    
    # Return results
    return {
        'significant': significant,
        'group1_stats': group1_stats,
        'group2_stats': group2_stats,
        'ax_boxplot': ax_boxplot,
        'ax_histogram': ax_histogram
    }