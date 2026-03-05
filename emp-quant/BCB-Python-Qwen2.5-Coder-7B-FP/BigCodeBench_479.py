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
                index = random.randint(0, len(parts) - 2)
                start = parts[index].find(',') + 1
                end = parts[index + 1].find(',') if parts[index + 1].find(',') != -1 else len(parts[index + 1])
                length = end - start
                new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
                parts[index] = parts[index][:start] + new_substring + parts[index][end:]
                result.append((item, ','.join(parts)))
            else:
                result.append((item, item))
        else:
            length = len(item)
            new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
            result.append((item, new_substring))
    df = pd.DataFrame(result, columns=['Original String', 'Modified String'])
    return df
data_list = ['apple,banana,cherry', 'dog,cat', 'hello,world', 'single']