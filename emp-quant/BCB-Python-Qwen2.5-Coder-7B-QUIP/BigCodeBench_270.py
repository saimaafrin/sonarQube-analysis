
import re
from collections import Counter

def task_func(sentence):
    # Use regular expression to find all words in the sentence
    words = re.findall(r'\b\w+\b', sentence)
    # Count the occurrences of each word
    word_count = Counter(words)
    # Return the dictionary of word counts
    return dict(word_count)