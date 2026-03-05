
import pandas as pd
import random
import re

def task_func(data_list, seed=None):
    # Set random seed for reproducibility
    if seed is not None:
        random.seed(seed)

    # Split each string into substrings
    substrings = [re.split(r'\s*,\s*', s) for s in data_list]

    # Randomly select an operation to apply to each substring
    operations = ['remove', 'replace', 'shuffle', 'randomize']
    random_ops = [random.choice(operations) for _ in range(len(substrings))]

    # Apply the selected operation to each substring
    modified_substrings = []
    for sub, op in zip(substrings, random_ops):
        if op == 'remove':
            if len(sub) > 1:
                sub.pop(random.randint(0, len(sub) - 1))
        elif op == 'replace':
            sub[random.randint(0, len(sub) - 1)] = 'random_string'
        elif op == 'shuffle':
            random.shuffle(sub)
        elif op == 'randomize':
            sub = random.sample(sub, len(sub))
        modified_substrings.append(sub)

    # Join the modified substrings back into strings
    modified_strings = [', '.join(sub) for sub in modified_substrings]

    # Create a DataFrame with the original and modified strings
    df = pd.DataFrame({'Original String': data_list, 'Modified String': modified_strings})

    return df