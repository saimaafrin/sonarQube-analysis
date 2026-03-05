
import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    # Split the strings into words using regular expression to handle multiple spaces
    words1 = re.findall(r'\b\w+\b', text1)
    words2 = re.findall(r'\b\w+\b', text2)
    
    # Check if the number of words is the same
    if len(words1) != len(words2):
        return np.nan, np.nan
    
    # Perform the paired t-test
    t_statistic, p_value = ttest_rel(words1, words2)
    
    return t_statistic, p_value