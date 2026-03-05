
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
    # Convert the string to lowercase and split into words
    words_list = re.findall(r'\b\w+\b', s.lower())
    
    # Filter out only the English words
    english_words = [word for word in words_list if word in SAMPLE_ENGLISH_WORDS]
    
    # Get unique words
    unique_english_words = list(set(english_words))
    
    # Return up to n unique English words, or all if there are fewer than n
    return unique_english_words[:n]