import pandas as pd
import re
STOPWORDS = ["a", "an", "the", "in", "is", "are"]
def task_func(text):
    """
    Count the frequency of each word in a text after removing specific stopwords.
    """
    # Remove stopwords
    text = re.sub(r'\b(?:' + r'|'.join(STOPWORDS) + r')\b', '', text)
    # Tokenize text
    words = re.split(r'\W+', text)
    # Count word frequencies
    word_freq = pd.Series(words).value_counts()
    # Exclude stopwords
    word_freq = word_freq[word_freq.index.isin(words)]
    return word_freq
text = "The quick brown fox jumps over the lazy dog."