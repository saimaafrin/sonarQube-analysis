import re
from nltk.stem import PorterStemmer
import pandas as pd
def task_func(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric characters (except spaces), removing punctuation, and stemming each word to its root form.
    Stemming is done using the NLTK's PorterStemmer, which applies a series of rules to find the stem of each word.
    """
    # Create a new Series with the processed text data
    processed_text_series = pd.Series(dtype=str)

    # Create a PorterStemmer object
    stemmer = PorterStemmer()

    # Iterate over each word in the text series
    for word in text_series:
        # Remove non-alphanumeric characters (except spaces)
        word = re.sub(r'[^a-zA-Z0-9 ]', '', word)

        # Remove punctuation
        word = re.sub(r'[^\w\s]', '', word)

        # Convert to lowercase
        word = word.lower()

        # Stem the word
        stemmed_word = stemmer.stem(word)

        # Add the stemmed word to the processed text series
        processed_text_series = processed_text_series.append(stemmed_word)

    return processed_text_series
text_series = pd.Series(['This', 'is', 'a', 'test', 'string'])