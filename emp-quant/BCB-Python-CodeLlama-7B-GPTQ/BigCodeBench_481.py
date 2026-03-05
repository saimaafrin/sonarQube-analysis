import pandas as pd
import random
import re
def task_func(data_list, seed=42):
    """
    Randomizes the order of comma-separated substrings within each string in a list, normalizing spaces to ensure a single space follows each comma using regex, then returns a DataFrame comparing original and randomized strings.
    """
    random.seed(seed)
    data_list = [re.sub(r",\s+", ", ", s) for s in data_list]
    random.shuffle(data_list)
    return pd.DataFrame({'Original String': data_list, 'Randomized String': data_list})
data_list = ['a, b, c', 'd, e, f', 'g, h, i']