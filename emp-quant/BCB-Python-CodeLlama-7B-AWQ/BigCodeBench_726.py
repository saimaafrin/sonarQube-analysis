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
    words = s.split()
    # Create a set of all the words in the string
    word_set = set(words)
    # Remove any non-English words
    english_words = [word for word in word_set if word.lower() in SAMPLE_ENGLISH_WORDS]
    # Return up to n English words
    return sample(english_words, n)