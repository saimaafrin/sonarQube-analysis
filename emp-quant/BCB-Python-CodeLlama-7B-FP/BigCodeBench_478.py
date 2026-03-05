import pandas as pd
import re
import random
def task_func(data_list, seed=None):
    """
    Removes a random comma-separated value (treated as a "substring") from each string in a list and returns a pandas DataFrame containing the original and modified strings.
    """
    if seed is not None:
        random.seed(seed)
    data_list = [re.sub(r',\w+', '', x) for x in data_list]
    df = pd.DataFrame({'Original String': data_list, 'Modified String': data_list})
    return df
data_list = ['a,b,c', 'd,e,f', 'g,h,i']