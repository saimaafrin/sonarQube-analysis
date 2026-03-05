
import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))

def task_func(input_string):
    # Split the input string into individual lines
    lines = input_string.split('\n')
    
    # Initialize an empty list to hold all words
    all_words = []
    
    # Process each line
    for line in lines:
        # Remove stopwords and split the line into words
        words = re.findall(r'\b\w+\b', line)
        words = [word.lower() for word in words if word.lower() not in STOPWORDS]
        all_words.extend(words)
    
    # Count the frequency of each word
    word_count = Counter(all_words)
    
    # Return the dictionary of word frequencies
    return dict(word_count)