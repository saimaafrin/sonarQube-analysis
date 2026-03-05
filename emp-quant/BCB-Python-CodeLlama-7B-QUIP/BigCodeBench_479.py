
import random
import string
import pandas as pd

def task_func(data_list, seed=0):
    random.seed(seed)
    original_strings = data_list
    modified_strings = [random_string(original_string) for original_string in original_strings]
    return pd.DataFrame({'Original String': original_strings, 'Modified String': modified_strings})

def random_string(original_string):
    start_index = random.randint(0, len(original_string))
    end_index = random.randint(start_index, len(original_string))
    random_substring = original_string[start_index:end_index]
    random_string = original_string[:start_index] + random_substring + original_string[end_index:]
    return random_string