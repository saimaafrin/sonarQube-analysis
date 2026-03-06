
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
    # Split the string into words
    words = re.split(r'\W+', s)
    # Filter out non-English words
    english_words = [word for word in words if word.lower() in SAMPLE_ENGLISH_WORDS]
    # Return up to n distinct English words
    return sample(english_words, n)