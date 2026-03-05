import re
import random
from nltk.corpus import words
from random import sample
import nltk
SAMPLE_ENGLISH_WORDS = set(words.words())
def task_func(s, n):
    # Split the string into words and convert to lowercase
    words_list = re.findall(r'\b\w+\b', s.lower())
    # Filter out non-English words
    english_words = [word for word in words_list if word in SAMPLE_ENGLISH_WORDS]
    # Get unique words
    unique_english_words = list(set(english_words))
    # Return up to n unique English words
    return sample(unique_english_words, min(n, len(unique_english_words)))