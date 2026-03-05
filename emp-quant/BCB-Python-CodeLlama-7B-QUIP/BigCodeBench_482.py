
import pandas as pd
import random
import re

def task_func(data_list, seed=None):
    df = pd.DataFrame({'Original String': data_list})
    random.seed(seed)
    for i in range(len(df)):
        row = df.iloc[i]
        original_string = row['Original String']
        modified_string = original_string
        substrings = re.split(r'\s*,\s*', original_string)
        if len(substrings) == 1:
            continue
        operation = random.choice(['remove', 'replace', 'shuffle', 'randomize'])
        if operation == 'remove':
            index = random.randint(0, len(substrings) - 1)
            substrings.pop(index)
        elif operation == 'replace':
            index = random.randint(0, len(substrings) - 1)
            substrings[index] = 'random_string'
        elif operation == 'shuffle':
            substrings = random.shuffle(substrings)
        elif operation == 'randomize':
            substrings = random.sample(substrings, len(substrings))
        modified_string = ', '.join(substrings)
        df.loc[i, 'Modified String'] = modified_string
    return df