
import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)
    
    def replace_random_substring(s):
        if ',' in s:
            parts = s.split(',')
            start_index = random.randint(0, len(parts) - 1)
            end_index = random.randint(start_index, len(parts) - 1)
            length = sum(len(part) for part in parts[start_index:end_index + 1])
            new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
            return ','.join(parts[:start_index] + [new_substring] + parts[end_index + 1:])
        else:
            length = len(s)
            new_substring = ''.join(random.choices(string.ascii_lowercase, k=length))
            return new_substring
    
    modified_strings = [replace_random_substring(s) for s in data_list]
    
    result_df = pd.DataFrame({
        'Original String': data_list,
        'Modified String': modified_strings
    })
    
    return result_df