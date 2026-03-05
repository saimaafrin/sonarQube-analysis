
import re
from collections import Counter

def task_func(sentence):
    """
    Count the occurrence of each word in a sentence and return the result as a dictionary.

    Args:
        sentence (str): The sentence to count words from.

    Returns:
        dict: A dictionary where the keys are the words and the values are their counts.
    """
    words = re.findall(r'\w+', sentence)
    return Counter(words)