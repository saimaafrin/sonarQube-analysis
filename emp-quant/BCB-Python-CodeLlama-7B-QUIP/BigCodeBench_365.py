
from collections import Counter
import json
import random
# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    random.seed(seed)
    random_words = random.sample(WORDS, n)
    with open(file_name, 'w') as f:
        json.dump(random_words, f)
    return file_name