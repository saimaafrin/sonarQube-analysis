
import re
import random
from nltk.corpus import words
from random import sample
# Ensure the words corpus is downloaded
import nltk
nltk.download('words')
# Constants
SAMPLE_ENGLISH_WORDS = set(words.words())  # Correct initialization
def task_func(s, n):
    """
    Extract up to n different English words from a string, ignoring case.
    The string is split into words and only the English words are retained.
    If there are fewer than n different English words, all distinct ones are returned.
    :param s: The input string
    :param n: The maximum number of words to extract
    :return: A list of up to n different English words found in the string
    """
    # Split the input string into individual words
    words = re.split(r'\W+', s)
    # Filter out non-English words
    english_words = [word for word in words if word.lower() in SAMPLE_ENGLISH_WORDS]
    # Return a random sample of up to n distinct English words
    return sample(english_words, n)