
import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    # Split the strings into words
    words1 = re.split(r'\W+', text1)
    words2 = re.split(r'\W+', text2)

    # Check if the strings have the same number of words
    if len(words1) != len(words2):
        return np.nan, np.nan

    # Perform the paired t-test
    t_statistic, p_value = ttest_rel(words1, words2)

    return t_statistic, p_value