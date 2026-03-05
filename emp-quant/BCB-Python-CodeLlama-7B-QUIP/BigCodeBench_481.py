
import pandas as pd
import random
import re

def task_func(data_list, seed=42):
    random.seed(seed)
    randomized_strings = []
    for string in data_list:
        randomized_string = re.sub(r'\s*,\s*', ' ', string)
        randomized_strings.append(randomized_string)
    randomized_strings = pd.DataFrame({'Original String': data_list, 'Randomized String': randomized_strings})
    return randomized_strings