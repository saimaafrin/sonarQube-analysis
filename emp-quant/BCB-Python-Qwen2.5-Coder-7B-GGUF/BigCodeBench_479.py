
import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)
    result = []
    for item in data_list:
        if ',' in item:
            parts = item.split(',')
            if len(parts) > 1:
                index = random.randint(0, len(parts) - 1)
                length = len(parts[index])
                new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
                parts[index] = new_substring
                modified_item = ','.join(parts)
            else:
                modified_item = item
        else:
            length = len(item)
            new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
            modified_item = new_substring
        result.append({'Original String': item, 'Modified String': modified_item})
    return pd.DataFrame(result)