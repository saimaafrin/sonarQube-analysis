
import re
from collections import Counter

def task_func(text, top_n):
    # Remove URLs from the text
    text = re.sub(r'http[s]?://.*[\s/]', ' ', text)
    # Tokenize the text
    tokens = re.split(r'\W+', text)
    # Count the top N words
    counter = Counter(tokens)
    return counter.most_common(top_n)