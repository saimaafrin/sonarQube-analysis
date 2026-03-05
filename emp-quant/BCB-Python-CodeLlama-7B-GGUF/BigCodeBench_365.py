
from collections import Counter
import json
import random
# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']
def task_func(n, file_name, seed=77):
    # Generate a list of n random words from the WORDS list
    random.seed(seed)
    random_words = random.sample(WORDS, n)
    # Create a dictionary with the random words as keys and their counts as values
    word_counts = Counter(random_words)
    # Write the dictionary to a JSON file
    with open(file_name, 'w') as f:
        json.dump(word_counts, f)
    return file_name