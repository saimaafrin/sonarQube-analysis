import re
import numpy as np
from scipy.stats import ttest_rel
def task_func(text1, text2):
    """
    Perform a paired t-test for the number of words in two strings, only if the strings produce the same number of words.
    The function should output with:
        t_statistic (float): The t-statistic, or NaN if tests cannot be performed due to unequal lengths.
        p_value (float): The p-value, or NaN if tests cannot be performed due to unequal lengths.
    """
    # Split the input strings into words
    words1 = re.split(r'\W+', text1)
    words2 = re.split(r'\W+', text2)

    # Check if the strings have the same number of words
    if len(words1) != len(words2):
        return np.nan, np.nan

    # Perform the paired t-test
    t_statistic, p_value = ttest_rel(words1, words2)

    return t_statistic, p_value
text1 = "This is a test string."
text2 = "This is another test string."