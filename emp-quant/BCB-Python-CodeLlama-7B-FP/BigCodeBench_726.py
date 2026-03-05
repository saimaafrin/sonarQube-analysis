import re
import random
from nltk.corpus import words
from random import sample
import nltk
SAMPLE_ENGLISH_WORDS = set(words.words())
def task_func(s, n):
    """
    Extract up to n different English words from a string, ignoring case.
    The string is split into words and only the English words are retained.
    If there are fewer than n different English words, all distinct ones are returned.
    """
    # Split the string into words
    words = re.split(r'\W+', s)
    # Remove non-English words
    words = [word for word in words if word.lower() in SAMPLE_ENGLISH_WORDS]
    # Remove duplicates
    words = list(set(words))
    # Return up to n words
    return sample(words, min(n, len(words)))