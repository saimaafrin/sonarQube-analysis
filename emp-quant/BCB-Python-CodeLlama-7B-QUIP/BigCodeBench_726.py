
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
    # Remove all non-English words
    english_words = re.findall(r'\w+', s)
    # Remove duplicates
    unique_english_words = list(set(english_words))
    # Sample up to n unique English words
    sample_english_words = sample(unique_english_words, n)
    return sample_english_words