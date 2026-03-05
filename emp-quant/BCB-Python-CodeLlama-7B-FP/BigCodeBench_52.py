import pandas as pd
import re
STOPWORDS = ["a", "an", "the", "in", "is", "are"]
def task_func(text):
    """
    Count the frequency of each word in a text after removing specific stopwords.
    """
    # Remove stopwords
    text = re.sub(r"\b(" + "|".join(STOPWORDS) + r")\b", "", text)
    # Tokenize text
    tokens = re.split(r"\W+", text)
    # Create a Series with word frequencies
    series = pd.Series(tokens).value_counts()
    return series