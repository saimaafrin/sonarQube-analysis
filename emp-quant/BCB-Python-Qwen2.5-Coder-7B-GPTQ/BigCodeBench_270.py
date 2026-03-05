import re
from collections import Counter
def task_func(sentence):
    # Use regular expression to find words in the sentence
    words = re.findall(r'\b\w+\b', sentence)
    # Use Counter to count occurrences of each word
    word_count = Counter(words)
    return word_count