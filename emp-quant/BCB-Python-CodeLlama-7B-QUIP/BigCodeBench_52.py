
import pandas as pd
import regex as re
# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]
def task_func(text):
    # Remove stopwords
    text = re.sub(r'\b' + '|'.join(STOPWORDS) + r'\b', '', text)
    # Tokenize and count word frequencies
    words = re.findall(r'\w+', text)
    word_counts = pd.Series(words).value_counts()
    return word_counts