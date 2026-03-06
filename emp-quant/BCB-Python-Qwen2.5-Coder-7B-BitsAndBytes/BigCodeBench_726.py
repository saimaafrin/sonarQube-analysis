
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
    Extracts up to n different English words from a string, ignoring case.
    
    Parameters:
    s (str): The input string to extract words from.
    n (int): The maximum number of different English words to return.
    
    Returns:
    List[str]: A list of up to n different English words found in the string.
    """
    # Split the string into words and convert to lowercase
    word_list = re.findall(r'\b\w+\b', s.lower())
    
    # Filter out non-English words
    english_words = [word for word in word_list if word in SAMPLE_ENGLISH_WORDS]
    
    # Get unique words
    unique_english_words = list(set(english_words))
    
    # Return up to n unique English words
    return sample(unique_english_words, min(n, len(unique_english_words)))