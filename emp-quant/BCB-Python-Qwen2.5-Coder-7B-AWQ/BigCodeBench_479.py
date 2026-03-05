import random
import string
import pandas as pd
def task_func(data_list, seed=0):
    random.seed(seed)
    result = []
    for original in data_list:
        if ',' in original:
            parts = original.split(',')
            if len(parts) > 1:
                index = random.randint(0, len(parts) - 2)
                length = len(parts[index])
                replacement = ''.join(random.choices(string.ascii_lowercase, k=length))
                modified = ','.join(parts[:index] + [replacement] + parts[index+1:])
                result.append({'Original String': original, 'Modified String': modified})
            else:
                result.append({'Original String': original, 'Modified String': original})
        else:
            length = len(original)
            replacement = ''.join(random.choices(string.ascii_lowercase, k=length))
            result.append({'Original String': original, 'Modified String': replacement})
    return pd.DataFrame(result)
data_list = ['apple,banana,cherry', 'dog,cat', 'hello']