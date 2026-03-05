
import pandas as pd
import regex as re
# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def task_func(text):
    # Remove stopwords and count the frequency of each word
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in STOPWORDS]
    word_counts = pd.Series(filtered_words).value_counts()
    
    return word_counts