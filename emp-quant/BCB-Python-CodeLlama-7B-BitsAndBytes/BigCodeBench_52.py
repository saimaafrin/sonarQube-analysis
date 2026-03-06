
import pandas as pd
import re

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def task_func(text):
    # Remove stopwords
    text = re.sub(r'\b(?:' + r'\b|\b'.join(STOPWORDS) + r')\b', '', text)

    # Tokenize text
    tokens = text.split()

    # Create a Series with word frequencies
    series = pd.Series(tokens).value_counts()

    return series