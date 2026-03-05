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
                start = parts[index].find(',') + 1
                end = parts[index + 1].find(',') if parts[index + 1].find(',') != -1 else len(parts[index + 1])
                length = end - start
                new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
                modified = original[:start] + new_substring + original[end:]
                result.append({'Original String': original, 'Modified String': modified})
        else:
            length = len(original)
            new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
            result.append({'Original String': original, 'Modified String': new_substring})
    return pd.DataFrame(result)
data_list = [
    "apple,banana,cherry",
    "dog,cat",
    "hello,world",
    "single"
]