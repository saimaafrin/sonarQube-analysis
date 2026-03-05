
from collections import Counter
import json
import random
# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def task_func(n, file_name, seed=77):
    random.seed(seed)
    selected_words = random.sample(WORDS, n)
    word_count = Counter(selected_words)
    
    with open(file_name, 'w') as json_file:
        json.dump(word_count, json_file, indent=4)
    
    return file_name