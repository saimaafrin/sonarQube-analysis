
import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

def ttest_two_sample(group1, group2, alpha=0.05):
    # Check if either group is empty or contains only NaN values
    if len(group1) < 2 or len(group2) < 2:
        raise ValueError("Either group is empty or contains only NaN values")

    # Remove NaN values from the groups
    group1_nan_free = np.nan_to_num(group1)
    group2_nan_free = np.nan_to_num(group2)

    # Check if there are enough non-NaN values in each group
    if len(group1_nan_free) < 2 or len(group2_nan_free) < 2:
        raise ValueError("One or both groups have less than two non-NaN values")

    # Check if the variance in each group is above a threshold
    if np.var(group1_nan_free) < 1e-8 or np.var(group2_nan_free) < 1e-8:
        raise ValueError("One or both groups have insufficient variance")

    # Perform the t-test
    ttest_result = ttest_ind(group1_nan_free, group2_nan_free, nan_policy='omit')

    # Check if the t-test is significant
    if ttest_result.pvalue > alpha:
        return {'significant': False, 'group1_stats': {'mean': ttest_result.statistic[0], 'std': ttest_result.statistic[1]}, 'group2_stats': {'mean': ttest_result.statistic[2], 'std': ttest_result.statistic[3]}, 'ax_boxplot': None, 'ax_histogram': None}
    else:
        # Generate a boxplot and histogram for data visualization
        fig, ax = plt.subplots(2, 1, figsize=(8, 8))
        ax[0].boxplot(group1_nan_free, group2_nan_free)
        ax[1].hist(group1_nan_free, group2_nan_free)
        return {'significant': True, 'group1_stats': {'mean': ttest_result.statistic[0], 'std': ttest_result.statistic[1]}, 'group2_stats': {'mean': ttest_result.statistic[2], 'std': ttest_result.statistic[3]}, 'ax_boxplot': ax[0], 'ax_histogram': ax[1]}

# Print the results
print(result)