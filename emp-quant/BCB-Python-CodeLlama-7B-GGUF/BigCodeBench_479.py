
import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)
    modified_list = []
    for data in data_list:
        # Find the first comma
        first_comma = data.find(',')
        # Find the second comma or the end of the string
        second_comma = data.find(',', first_comma + 1)
        if second_comma == -1:
            second_comma = len(data)
        # Replace the substring with a random string
        modified_list.append(data[:first_comma] + ''.join(random.choice(string.ascii_lowercase) for _ in range(second_comma - first_comma)) + data[second_comma:])
    return pd.DataFrame({'Original String': data_list, 'Modified String': modified_list})