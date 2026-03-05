
import re
from nltk.stem import PorterStemmer
import pandas as pd

def task_func(text_series):
    # Lowercase all letters
    text_series = text_series.str.lower()
    
    # Remove non-alphanumeric characters except spaces
    text_series = text_series.str.replace(r'[^a-zA-Z\s]', '')
    
    # Remove punctuation
    text_series = text_series.str.replace(r'[^\w\s]', '')
    
    # Stem each word
    stemmer = PorterStemmer()
    text_series = text_series.apply(lambda x: ' '.join([stemmer.stem(word) for word in x.split()]))
    
    return text_series