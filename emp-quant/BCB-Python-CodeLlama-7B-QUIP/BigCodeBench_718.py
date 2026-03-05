
import re
import numpy as np
from scipy.stats import ttest_rel

def task_func(text1, text2):
    # Remove all non-alphanumeric characters from the text
    text1 = re.sub(r'[^a-zA-Z0-9]', '', text1)
    text2 = re.sub(r'[^a-zA-Z0-9]', '', text2)

    # Convert the text to lowercase
    text1 = text1.lower()
    text2 = text2.lower()

    # Tokenize the text into individual words
    words1 = text1.split()
    words2 = text2.split()

    # Check if the number of words is equal
    if len(words1) != len(words2):
        return np.nan, np.nan

    # Calculate the t-statistic and p-value
    t_statistic, p_value = ttest_rel(words1, words2)

    return t_statistic, p_value