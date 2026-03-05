import re
import random
from nltk.corpus import words
from random import sample
import nltk
def task_func(s, n):
    """
    Extract up to n different English words from a string, ignoring case.
    The string is split into words and only the English words are retained.
    If there are fewer than n different English words, all distinct ones are returned.
    """
    # Split the string into words
    words = re.split(r'\W+', s)
    # Remove any empty strings
    words = [word for word in words if word]
    # Convert all words to lowercase
    words = [word.lower() for word in words]
    # Remove any duplicate words
    words = list(set(words))
    # Return up to n random words
    return sample(words, n)