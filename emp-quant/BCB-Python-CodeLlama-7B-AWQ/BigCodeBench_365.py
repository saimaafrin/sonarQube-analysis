from collections import Counter
import json
import random
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    """
    Generate a json file with n randomly selected words from the WORDS constant list.
    """
    random.seed(seed)
    word_list = random.sample(WORDS, n)
    with open(file_name, 'w') as f:
        json.dump(word_list, f)
    return file_name