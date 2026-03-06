
import re
from nltk.tokenize import word_tokenize
from collections import Counter

def task_func(input_str):
    # Remove all special characters, punctuation marks, and spaces
    cleaned_str = re.sub(r'[^\w\s]', '', input_str)
    
    # Tokenize the cleaned string into words
    words = word_tokenize(cleaned_str.lower())
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    return word_count