
import pandas as pd
import re
import random

def task_func(data_list, seed=None):
    random.seed(seed)
    data_list = [re.sub(r',\s*[a-zA-Z]+\s*', '', x) for x in data_list]
    return pd.DataFrame({'Original String': data_list, 'Modified String': data_list})