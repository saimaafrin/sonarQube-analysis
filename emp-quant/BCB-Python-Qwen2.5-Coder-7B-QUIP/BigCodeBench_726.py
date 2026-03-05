
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
    # Split the string into words and filter out non-English words
    words = re.findall(r'\b\w+\b', s.lower())
    english_words = [word for word in words if word in SAMPLE_ENGLISH_WORDS]
    
    # Return up to n different English words
    return list(set(english_words) if len(english_words) > n else english_words[:n])