
from nltk.tokenize import RegexpTokenizer
from collections import Counter

def task_func(text):
    # Tokenize the text using regular expression to capture words starting with $ followed by alphanumeric characters
    tokenizer = RegexpTokenizer(r'\$\w+')
    tokens = tokenizer.tokenize(text)
    
    # Filter out tokens that consist solely of $ symbol
    filtered_tokens = [token[1:] for token in tokens if len(token) > 1]
    
    # Count the occurrences of each word
    word_counts = Counter(filtered_tokens)
    
    # Get the five most common words
    most_common_words = word_counts.most_common(5)
    
    return most_common_words