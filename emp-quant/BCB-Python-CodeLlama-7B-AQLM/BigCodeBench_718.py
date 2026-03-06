import re
import numpy as np
from scipy.stats import ttest_rel
def task_func(text1, text2):
    """
    Perform a paired t-test for the number of words in two strings, only if the strings produce the same number of words.
    
    Parameters:
    - text1 (str), text2 (str): The two text strings.
    
    Returns:
    - t_statistic (float): The t-statistic, or NaN if tests cannot be performed due to unequal lengths.
    - p_value (float): The p-value, or NaN if tests cannot be performed due to unequal lengths.
    
    Requirements:
    - re
    - numpy
    - scipy
    
    Example:
    >>> task_func('Words, words, words.', 'And more words!')
    (1.7320508075688774, 0.22540333075851657)
    """
    # Split the strings into words.
    words1 = re.findall(r'\w+', text1)
    words2 = re.findall(r'\w+', text2)
    
    # Check if the lengths are equal.
    if len(words1) != len(words2):
        return np.nan, np.nan
    
    # Perform the t-test.
    t_statistic, p_value = ttest_rel(words1, words2)
    
    return t_statistic, p_value