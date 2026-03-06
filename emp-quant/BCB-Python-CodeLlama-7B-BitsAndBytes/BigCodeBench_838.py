
import re
from nltk.stem import PorterStemmer
import pandas as pd

def task_func(text_series):
    # Create a new Series with the processed text
    processed_text = pd.Series(text_series.apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x.lower())))

    # Remove punctuation and stem each word
    stemmer = PorterStemmer()
    processed_text = processed_text.apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))

    return processed_text