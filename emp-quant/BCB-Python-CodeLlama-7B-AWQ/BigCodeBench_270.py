import re
from collections import Counter
def task_func(sentence):
    """
    Count the occurrence of each word in a sentence and return the result as a dictionary.
    This function uses a regular expression to find words and a Counter to count their occurrences.
    """
    words = re.findall(r'\w+', sentence)
    word_counts = Counter(words)
    return word_counts