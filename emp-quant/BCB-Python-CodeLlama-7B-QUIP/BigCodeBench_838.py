
import re
from nltk.stem import PorterStemmer

def task_func(text_series):
    # Remove non-alphanumeric characters and convert to lowercase
    text_series = re.sub(r'[^a-zA-Z0-9]', '', text_series).lower()

    # Remove punctuation
    text_series = re.sub(r'[.!?]', '', text_series)

    # Stem each word in the text
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in text_series.split()]

    # Join the stemmed words back together
    stemmed_text = " ".join(stemmed_words)

    return stemmed_text