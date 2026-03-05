
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenize the text into words using a regular expression that matches dollar-prefixed words
    tokenizer = RegexpTokenizer(r'\b\$[a-zA-Z0-9]+\b')
    words = tokenizer.tokenize(text)
    
    # Filter out words that start with a dollar symbol and are not followed by alphanumeric characters
    dollar_words = [word[1:] for word in words if word.startswith('$') and word[1:].isalnum()]
    
    # Count the frequency of each dollar-prefixed word
    word_counts = Counter(dollar_words)
    
    # Get the five most common dollar-prefixed words
    most_common_words = word_counts.most_common(5)
    
    return most_common_words