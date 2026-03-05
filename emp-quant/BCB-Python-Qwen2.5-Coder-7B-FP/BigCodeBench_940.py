import re
from nltk import word_tokenize
from collections import Counter
def task_func(input_str):
    # Remove all special characters, punctuation marks and spaces
    cleaned_str = re.sub(r'[^\w\s]', '', input_str)
    cleaned_str = re.sub(r'\s+', ' ', cleaned_str).strip()
    
    # Tokenize the cleaned string into words
    words = word_tokenize(cleaned_str)
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    return word_count