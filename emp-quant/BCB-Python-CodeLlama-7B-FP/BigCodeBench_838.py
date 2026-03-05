import re
from nltk.stem import PorterStemmer
import pandas as pd
def task_func(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric characters (except spaces), removing punctuation, and stemming each word to its root form.
    Stemming is done using the NLTK's PorterStemmer, which applies a series of rules to find the stem of each word.
    The function should output with:
        pandas.Series: A Series where each string has been processed to remove non-alphanumeric characters,
        punctuation, converted to lowercase, and where each word has been stemmed.
    """
    # Create a PorterStemmer object
    stemmer = PorterStemmer()

    # Create a regular expression pattern to remove non-alphanumeric characters (except spaces)
    pattern = re.compile('[^a-zA-Z0-9\s]')

    # Create a regular expression pattern to remove punctuation
    punctuation_pattern = re.compile('[^\w\s]')

    # Create a list to store the processed text
    processed_text = []

    # Iterate over each string in the text series
    for text in text_series:
        # Convert the string to lowercase
        text = text.lower()

        # Remove non-alphanumeric characters (except spaces) using the regular expression pattern
        text = re.sub(pattern, '', text)

        # Remove punctuation using the regular expression pattern
        text = re.sub(punctuation_pattern, '', text)

        # Tokenize the text into individual words
        words = text.split()

        # Stem each word using the PorterStemmer
        stemmed_words = [stemmer.stem(word) for word in words]

        # Join the stemmed words back into a string
        processed_text.append(' '.join(stemmed_words))

    # Create a new pandas Series with the processed text
    processed_text_series = pd.Series(processed_text)

    return processed_text_series
text_series = pd.Series(['This is a test sentence.', 'This is another test sentence.'])